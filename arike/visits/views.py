from datetime import datetime, timedelta
from distutils.log import Log
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from arike.patients.models import Patient

from arike.treatments.models import PatientDisease, Treatment, TreatmentNote
from arike.visits.forms import TreatmentNoteCreationForm, VisitDetailCreationForm, VisitScheduleForm
from arike.visits.models import VisitDetail, VisitSchedule 
from arike.treatments.views import AuthorisedDiseaseHistoryManager
class AuthorisedVisitScheduleManager(LoginRequiredMixin, PermissionRequiredMixin):
    pass

class SchedulesView(LoginRequiredMixin, ListView):
    template_name = "visits/schedules.html"
    context_object_name = "patient_diseases"

    def get_queryset(self):
        return PatientDisease.objects.filter(deleted=False, treatment__given_by=self.request.user)

class ScheduleVisitView(AuthorisedVisitScheduleManager, CreateView):
    permission_required = "visits.add_visitschedule"
    form_class = VisitScheduleForm
    template_name = "visits/schedule_visit.html"
    success_url = "/visits/upcoming"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['uid'])
        context['treatments'] = Treatment.objects.filter(patient=self.kwargs["uid"], given_by=self.request.user, deleted=False)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.patient = Patient.objects.get(pk=self.kwargs['uid'])
        self.object.nurse = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class UpcomingVisitsView(LoginRequiredMixin, ListView):
    template_name = "visits/upcoming_visits.html"
    
    def get_queryset(self):
        return VisitSchedule.objects.filter(deleted=False, nurse=self.request.user, date__gte=datetime.now().date())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        querysets = self.get_queryset()
        context['today'] = querysets.filter(date=datetime.now().date(), time=datetime.now().time())
        context['tomorrow'] = querysets.filter(date=datetime.now().date() + timedelta(days=1))
        context['next_week'] = querysets.filter(date__gte=datetime.now().date() + timedelta(days=7))
        return context

class VisitView(LoginRequiredMixin, TemplateView):
    template_name = "visits/visit.html"

def unschedule_visit(request, uid, vid):
    print(uid, vid)
    schedule = VisitSchedule.objects.filter(pk=vid, deleted=False, nurse=request.user, patient=uid)
    if schedule.exists():
        schedule.update(deleted=True)
    return HttpResponse("OK")

class CreatePatientHealthInfoView(AuthorisedVisitScheduleManager, CreateView):
    permission_required = "visits.add_visitdetail"
    form_class = VisitDetailCreationForm
    template_name = "visits/create_patient_health.html"

    def get_success_url(self):
        return f"/visits/{self.kwargs['uid']}/visit/{self.kwargs['vid']}"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.visit_schedule = VisitSchedule.objects.get(pk=self.kwargs['vid'])
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ActiveTreatmentsView(LoginRequiredMixin, ListView):
    context_object_name = "treatments"
    template_name = "visits/active_treatments.html"
    
    def get_queryset(self):
        return Treatment.objects.filter(deleted=False, patient=self.kwargs['uid'])

class TreatmentDetailView(LoginRequiredMixin, DetailView):
    model = Treatment
    template_name = "visits/treatment_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = TreatmentNote.objects.filter(treatment=self.kwargs['pk'])
        return context


class CreateTreatmentNoteView(AuthorisedDiseaseHistoryManager, CreateView):
    permission_required = "treatments.add_treatmentnote"
    form_class = TreatmentNoteCreationForm
    template_name = "visits/create_treatment_note.html"

    def get_success_url(self):
        return f"/visits/{self.kwargs['uid']}/visit/{self.kwargs['vid']}/treatments"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['treatment'] = Treatment.objects.get(pk=self.kwargs['tid'])
        return context 

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.treatment = Treatment.objects.get(pk=self.kwargs['tid'])
        self.object.visit_details = VisitDetail.objects.get(pk=self.kwargs['vid'])
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


