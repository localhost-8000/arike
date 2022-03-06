from django.urls import path

from arike.visits.views import (
    ActiveTreatmentsView,
    CreatePatientHealthInfoView,
    CreateTreatmentNoteView,
    ScheduleVisitView,
    SchedulesView,
    TreatmentDetailView,
    UpcomingVisitsView,
    VisitView,
    unschedule_visit,
)

app_name = "visits"

urlpatterns = [
    path("", SchedulesView.as_view(), name="schedules"),
    path("upcoming", UpcomingVisitsView.as_view(), name="upcoming_visits"),
    path("<int:uid>/schedule", ScheduleVisitView.as_view(), name="schedule_visit"),
    path("<int:uid>/visit/<int:vid>", VisitView.as_view(), name="visit"),
    path("<int:uid>/visit/<int:vid>/delete", unschedule_visit, name="unschedule_visit"),
    path("<int:uid>/visit/<int:vid>/health-info", CreatePatientHealthInfoView.as_view(), name="create_patient_health_info"),
    path("<int:uid>/visit/<int:vid>/treatments", ActiveTreatmentsView.as_view(), name="treatment_note"),
    path("<int:uid>/visit/<int:vid>/treatments/<pk>", TreatmentDetailView.as_view(), name="treatment_details"),
    path("<int:uid>/visit/<int:vid>/treatments/<int:tid>/note", CreateTreatmentNoteView.as_view(), name="create_treatment_note"),
]
