from django.contrib.auth.views import LogoutView
from django.urls import path

from arike.home.views import (
    ActivateAccountView,
    DashboardView,
    UserLoginView,
    UserProfileWithPasswordChangeView,
)

app_name = "home"

urlpatterns = [
    path("", DashboardView.as_view(), name="home_dashboard"),
    path("login", UserLoginView.as_view(), name="login_user"),
    path("logout", LogoutView.as_view(), name="logout_user"),
    path("account/<pk>", UserProfileWithPasswordChangeView.as_view(), name="user_profile"),
    path("account/activate/<uidb64>/<token>/", ActivateAccountView.as_view(), name="activate_account"),
]
