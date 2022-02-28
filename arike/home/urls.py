from django.urls import path
from arike.home.views import UserProfileView, UserProfileWithPasswordChangeView
from django.contrib.auth.views import LogoutView

from home.views import UserLoginView, get_view

app_name = "home"

urlpatterns = [
    path("", get_view, name="home"),
    path("login", UserLoginView.as_view(), name="login_user"),
    path("logout", LogoutView.as_view(), name="logout_user"),
    path("profile/<pk>", UserProfileWithPasswordChangeView.as_view(), name="user_profile"),
]