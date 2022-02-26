from unicodedata import name
from django.urls import path

from arike.users.views import (
    GenericUserAssignView,
    GenericUserCreateView,
    GenericUserDeleteView,
    GenericUserDetailView,
    GenericUserUpdateView,
    GenericUsersView,
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
    path("", GenericUsersView.as_view(), name="users"),
    path("create", GenericUserCreateView.as_view(), name="create_user"),
    path("<pk>", GenericUserDetailView.as_view(), name="detail_user"),
    path("update/<pk>", GenericUserUpdateView.as_view(), name="update_user"),
    path("delete/<pk>", GenericUserDeleteView.as_view(), name="delete_user"),
    path("create/assign", GenericUserAssignView.as_view(), name="assign_user"),
]
