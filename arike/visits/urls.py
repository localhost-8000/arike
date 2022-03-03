from django.urls import path

from arike.patients.views import (
    PatientCreateView,
    PatientDetailView,
    PatientsListView,
    PatientUpdateView,
)

app_name = "visits"

urlpatterns = [
    # path('', PatientsListView.as_view(), name='patients_list'),
    # path('create', PatientCreateView.as_view(), name='patient_create'),
    # path('<pk>', PatientDetailView.as_view(), name='patient_detail'),
    # path('update/<pk>', PatientUpdateView.as_view(), name='patient_update'),
]