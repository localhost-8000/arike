from django.contrib.auth.views import LogoutView
from django.urls import path

from arike.home.views import (
    DashboardView,
    UserLoginView,
    UserProfileWithPasswordChangeView,
    UserVerifyAndSetPasswordView,
)

app_name = "home"

urlpatterns = [
    path("", DashboardView.as_view(), name="home_dashboard"),
    path("login", UserLoginView.as_view(), name="login_user"),
    path("logout", LogoutView.as_view(), name="logout_user"),
    path("account/<pk>", UserProfileWithPasswordChangeView.as_view(), name="user_profile"),
    path("account/verify/<str:uid>/<uuid:token>", UserVerifyAndSetPasswordView.as_view(), name="verify_user"),
]
