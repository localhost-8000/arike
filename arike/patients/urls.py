from django.urls import path

from arike.patients.views import (
    PatientCreateView,
    PatientDetailView,
    PatientFamilyCreateView,
    PatientFamilyDeleteView,
    PatientFamilyListView,
    PatientFamilyUpdateView,
    PatientVisitHistoryDetailView,
    PatientVisitHistoryView,
    PatientsListView,
    PatientUpdateView,
)

app_name = "patients"

urlpatterns = [
    path('', PatientsListView.as_view(), name='patients_list'),
    path('create', PatientCreateView.as_view(), name='patient_create'),
    path('<pk>', PatientDetailView.as_view(), name='patient_detail'),
    path('update/<pk>', PatientUpdateView.as_view(), name='patient_update'),
    path('<int:uid>/family', PatientFamilyListView.as_view(), name='patient_family_list'),
    path('<int:uid>/family/create', PatientFamilyCreateView.as_view(), name='patient_family_create'),
    path('<int:uid>/family/delete/<pk>', PatientFamilyDeleteView.as_view(), name='patient_family_detail'),
    path('<int:uid>/family/update/<pk>', PatientFamilyUpdateView.as_view(), name='patient_family_update'),
    path('<int:uid>/visit/history', PatientVisitHistoryView.as_view(), name="patient_visit_history"),
    path('<int:uid>/visit/detail/<pk>', PatientVisitHistoryDetailView.as_view(), name="patient_visit_history_detail")
]
