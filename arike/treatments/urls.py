from django.urls import path

from arike.treatments.views import (
    DiseaseHistoryCreateView,
    DiseaseHistoryDeleteView,
    DiseaseHistoryListView,
    DiseaseHistoryUpdateView,
    TreatmentCreateView,
    TreatmentDeleteView,
    TreatmentListView,
    TreatmentUpdateView,
    load_treatment_care_sub_type,
)

app_name = "treatments"

urlpatterns = [
    path("<int:uid>/disease/history", DiseaseHistoryListView.as_view(), name="disease_history_ist"),
    path("<int:uid>/disease/history/create", DiseaseHistoryCreateView.as_view(), name="disease_history_create"),
    path("<int:uid>/disease/history/update/<pk>", DiseaseHistoryUpdateView.as_view(), name="disease_history_update"),
    path("<int:uid>/disease/history/delete/<pk>", DiseaseHistoryDeleteView.as_view(), name="disease_history_delete"),

    path("<int:uid>/disease/treatments", TreatmentListView.as_view(), name="treatment_list"),
    path("<int:uid>/disease/treatments/create", TreatmentCreateView.as_view(), name="treatment_create"),
    path("<int:uid>/disease/treatments/update/<pk>", TreatmentUpdateView.as_view(), name="treatment_update"),
    path("<int:uid>/disease/treatments/delete/<pk>", TreatmentDeleteView.as_view(), name="treatment_delete"),

    path("load/care_sub_types/", load_treatment_care_sub_type, name="load_care_sub_types"),
]
