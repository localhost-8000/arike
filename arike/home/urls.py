from django.urls import path

from home.views import UserLoginView, get_view

app_name = "home"

urlpatterns = [
    path("", get_view, name="home"),
    path("login", UserLoginView.as_view(), name="login_user"),
]