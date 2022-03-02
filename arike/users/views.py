
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import (
    HttpResponseBadRequest,
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from arike.facilities.models import Facility
from arike.users.forms import UserCreateForm, UserFacilityAssignForm

from uuid import uuid4
import base64

User = get_user_model()

# Users CRUD Operatins view...
class GenericUsersView(LoginRequiredMixin, ListView):
    template_name = "users/users.html"
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class GenericUserCreateView(LoginRequiredMixin, CreateView):
    form_class = UserCreateForm
    template_name = "users/create_user.html"
    success_url = "/users/create/assign"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data["email"])
        self.object.username = form.cleaned_data["email"]
        self.object.is_active = False
        self.object.save()

        self.send_verify_and_set_password_mail(self.object)

        return HttpResponseRedirect(self.get_success_url())

    def send_verify_and_set_password_mail(self, user):
        token = uuid4()
        uid = user.id
        self.request.session[str(uid)] = str(token)
        subject = "Welcome to Arike"
        print('link to verify: ', self.request.build_absolute_uri(f'/account/verify/{uid}/{token}'))
        message = f"Hello {user.first_name},\nAn account has been created for you on Arike.\n\nUsername: {user.username}\n\nPlease click the link below to verify your account and set a password for login.\n\n{self.request.build_absolute_uri(f'/account/verify/{uid}/{token}')}\n\nThank you."
        user.email_user(subject, message, 'rt945471@gmail.com')


class GenericUserUpdateView(UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = "users/update_user.html"
    success_url = "/users/"

    def form_valid(self, form):
        self.object = form.save()
        if "email" in form.changed_data:
            self.object.username = form.cleaned_data["email"]
            self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

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

# Assign user facility views...

class GenericUserAssignView(CreateView):
    form_class = UserFacilityAssignForm
    template_name = "users/assign_facility.html"

    def get(self, request, *args, **kwargs): 
        user_set = User.objects.filter(pk=kwargs['user_id'])
        
        if not user_set.exists():
            return HttpResponseNotFound("User not found")
        
        user = user_set[0]
        if not (not user.is_active and user.facility is None and user.role == 'none'):
            return HttpResponseBadRequest("You can only assign the facility after creating the user")

        query_param = request.GET.get("query_param")
        if query_param:
            self.query_results = Facility.objects.filter(Q(name__icontains=query_param) | Q(address__icontains=query_param))   
        
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.kwargs['user_id']
        if self.request.GET.get("query_param"):
            context["query_results"] = self.query_results
        return context

    def form_valid(self, form):
        facility = form.cleaned_data["facility"]
        role = form.cleaned_data["role"]

        # update user data and make the user active
        user = User.objects.filter(pk=self.kwargs['user_id'])
        user.update(
            facility=facility, 
            role=role, 
            is_active=True, 
            is_staff = True if form.cleaned_data["role"] == "district_admin" else False,
            is_superuser = True if form.cleaned_data["role"] == "district_admin" else False
        )

        return HttpResponsePermanentRedirect("/users/")

class GenericUserUpdateAssignView(UpdateView):
    model = User
    form_class = UserFacilityAssignForm
    template_name = "users/update_assigned_facility.html"
    success_url = "/users/"

    def get_object(self):
        return User.objects.get(pk=self.kwargs["user_id"])
    
    def get(self, request, *args, **kwargs): 
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
        self.object = form.save()
        self.object.is_staff = True if form.cleaned_data["role"] == "district_admin" else False
        self.object.is_superuser = True if form.cleaned_data["role"] == "district_admin" else False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
