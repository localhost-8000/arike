
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.http import HttpResponseNotAllowed, HttpResponsePermanentRedirect

from arike.home.forms import SetPasswordForm

User = get_user_model()
class UserLoginView(LoginView):
    template_name = 'users/user_login.html'

class UserProfileWithPasswordChangeView(PasswordChangeView):
    form_class = auth_forms.SetPasswordForm
    template_name = 'home/user_profile.html'
    success_url = '/users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = User.objects.get(pk=self.kwargs['pk'])
        return context

class UserVerifyAndUpdatePasswordView(UpdateView):
    form_class = SetPasswordForm
    template_name = 'home/user_verify_update.html'
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        token = kwargs['token']
        uid = kwargs['uid']

        if (not uid in self.request.session) or (self.request.session[uid] != str(token)):
            return HttpResponseNotAllowed("You are not allowed to access this page!")
        
        return super().get(request, *args, **kwargs)

    def get_object(self):
        user = User.objects.get(pk=self.kwargs['uid'])
        return user 
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.object
        return kwargs

    def form_valid(self, form):
        # Set the new password
        password = form.cleaned_data['new_password1']
        self.object.set_password(password)
        self.object.save()

        # Delete the uid and token from the session
        del self.request.session[self.kwargs['uid']]
        return HttpResponsePermanentRedirect(self.get_success_url())

def get_view(request):
    return render(request, 'pages/home.html')
