
from django.urls import path

from arike.users.views import (
    GenericUserAssignView,
    GenericUserCreateView,
    GenericUserDeleteView,
    GenericUserDetailView,
    GenericUserUpdateAssignView,
    GenericUserUpdateView,
    GenericUsersView,
)

app_name = "users"
urlpatterns = [
    path("", GenericUsersView.as_view(), name="users_list"),
    path("create", GenericUserCreateView.as_view(), name="create_user"),
    path("<pk>", GenericUserDetailView.as_view(), name="detail_user"),
    path("update/<pk>", GenericUserUpdateView.as_view(), name="update_user"),
    path("delete/<pk>", GenericUserDeleteView.as_view(), name="delete_user"),
    path("create/<int:user_id>/assign", GenericUserAssignView.as_view(), name="assign_facility"),
    path("update/<int:user_id>/assign", GenericUserUpdateAssignView.as_view(), name="update_assigned_facility"),
]
