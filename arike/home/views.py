
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render

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

def get_view(request):
    return render(request, 'pages/home.html')
