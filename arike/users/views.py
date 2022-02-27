
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ModelForm, ModelChoiceField
from django.http import HttpResponseBadRequest, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from arike.facilities.models import Facility
from arike.home.models import District
from django.db.models import Q

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

class GenericUsersView(ListView):
    template_name = "users/users.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class UserCreateForm(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "district"]
    
    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        if len(data) < 2:
            self.add_error("first_name", "First name must be at least 2 characters long")
        return data
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        if not data:
            self.add_error("email", "Email is required")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["first_name"].widget.attrs["placeholder"] = "Alex"
        # self.fields["last_name"].widget.attrs["placeholder"] = "Doe"
        # self.fields["email"].widget.attrs["placeholder"] = "mail@example.com"
        self.fields["district"] = ModelChoiceField(queryset=District.objects.all(), empty_label=None)

class UserFacilityAssignForm(ModelForm):

    class Meta:
        model = User 
        fields = ["facility", "role"]

    def clean_facility(self):
        data = self.cleaned_data["facility"]
        if not data:
            self.add_error("facility", "Facility is required")
        return data

    def clean_role(self):
        data = self.cleaned_data["role"]
        if not data or data == "none":
            self.add_error("role", "Role is required")
        return data

class GenericUserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = "users/create_user.html"
    success_url = "/users/create/assign"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data["email"])
        self.object.username = f"@{form.cleaned_data['first_name']}{form.cleaned_data['last_name']}"
        self.object.is_active = False
        self.object.save()

        self.request.session["is_second_step"] = True
        self.request.session["user_id"] = self.object.id

        return HttpResponseRedirect(self.get_success_url())

class GenericUserAssignView(CreateView):
    form_class = UserFacilityAssignForm
    template_name = "users/assign_facility.html"

    def get(self, request, *args, **kwargs): 
        if "is_second_step" not in self.request.session or not self.request.session["is_second_step"]:
            return HttpResponseBadRequest("You can only assign the facility after creating the user")

        query_param = request.GET.get("query_param")
        if query_param:
            self.query_results = Facility.objects.filter(Q(name__icontains=query_param) | Q(address__icontains=query_param))
            
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get("query_param"):
            context["query_results"] = self.query_results

        return context

    def form_valid(self, form):
        facility = form.cleaned_data["facility"]
        role = form.cleaned_data["role"]
        user_id = self.request.session["user_id"]

        # update user data and make the user active
        user = User.objects.filter(pk=user_id)
        user.update(facility=facility, role=role, is_active=True)

        # change the session variable to None
        self.request.session["is_second_step"] = False
        self.request.session["user_id"] = None

        return HttpResponsePermanentRedirect("/users/")

class GenericUserUpdateView(UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/update_user.html"
    success_url = "/users/"

class GenericUserDetailView(DetailView):
    model = User
    template_name = "users/detail_user.html"

class GenericUserDeleteView(DeleteView):
    model = User
    template_name = "users/delete_user.html"
    success_url = "/users/"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())