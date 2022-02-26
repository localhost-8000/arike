
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View


class UserLoginView(LoginView):
    template_name = 'users/user_login.html'

def get_view(request):
    return render(request, 'pages/home.html')