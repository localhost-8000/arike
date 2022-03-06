
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseNotAllowed,
    HttpResponsePermanentRedirect,
)
from arike.users.token import account_activation_token
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from arike.home.forms import SetPasswordForm

User = get_user_model()
class UserLoginView(LoginView):
    template_name = 'users/user_login.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "home/dashboard.html"

class UserProfileWithPasswordChangeView(PasswordChangeView):
    form_class = auth_forms.SetPasswordForm
    template_name = 'home/user_profile.html'
    success_url = '/users'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if self.request.user.id != user.id or user.is_active == False:
            return HttpResponseForbidden("You are not allowed to access this page")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = User.objects.get(pk=self.kwargs['pk'])
        return context

class ActivateAccountView(UpdateView):
    form_class = SetPasswordForm
    template_name = 'home/user_verify_update.html'
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None 
        if user is not None and account_activation_token.check_token(user, token):
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponse("Activation link is invalid!")
    
    def get_object(self):
        uid = force_text(urlsafe_base64_decode(self.kwargs['uidb64']))
        user = User.objects.get(pk=uid)
        return user 
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.object
        return kwargs

    def form_valid(self, form):
        # Set the new password
        password = form.cleaned_data['new_password1']
        self.object.set_password(password)
        self.object.is_verified = True
        self.object.save()

        return HttpResponsePermanentRedirect(self.get_success_url())
