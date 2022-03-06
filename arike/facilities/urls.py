from django.urls import path

from arike.facilities.views import (
    GenericFacilitiesView,
    GenericFacilityCreateView,
    GenericFacilityDeleteView,
    GenericFacilityDetailView,
    GenericFacilityUpdateView,
)

app_name = "facilities"

urlpatterns = [
    path("", GenericFacilitiesView.as_view(), name="facilities"),
    path("create/", GenericFacilityCreateView.as_view(), name="create_facility"),
    path("detail/<pk>", GenericFacilityDetailView.as_view(), name="facility_detail"),
    path("update/<pk>", GenericFacilityUpdateView.as_view(), name="update_facility"),
    path("delete/<pk>", GenericFacilityDeleteView.as_view(), name="delete_facility"),
]
