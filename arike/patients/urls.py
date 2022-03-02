from django.urls import path

from arike.patients.views import (
    PatientCreateView,
    PatientDeleteView,
    PatientDetailView,
    PatientsListView,
    PatientUpdateView,
)

app_name = "patients"

urlpatterns = [
    path('', PatientsListView.as_view(), name='patients_list'),
    path('create', PatientCreateView.as_view(), name='patient_create'),
    path('<pk>', PatientDetailView.as_view(), name='patient_detail'),
    path('update/<pk>', PatientUpdateView.as_view(), name='patient_update'),
    path('delete/<pk>', PatientDeleteView.as_view(), name='patient_delete'),
]
