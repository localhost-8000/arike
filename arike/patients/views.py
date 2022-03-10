from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from arike.patients.forms import PatientCreationForm, PatientFamilyCreationForm

from arike.patients.models import Patient, PatientFamily
from arike.treatments.models import TreatmentNote
from arike.visits.models import VisitDetail, VisitSchedule


class AuthorisedPatientManager(LoginRequiredMixin, PermissionRequiredMixin):
    pass 

class PatientsListView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'patients/patients.html'

    def get_queryset(self):
        return Patient.objects.filter(deleted=False)

class PatientCreateView(AuthorisedPatientManager, CreateView):
    permission_required = "patients.add_patient"
    model = Patient
    form_class = PatientCreationForm
    template_name = "patients/create_patient.html"
    success_url = "/patients/"

class PatientUpdateView(AuthorisedPatientManager, UpdateView):
    permission_required = "patients.change_patient"
    model = Patient
    form_class = PatientCreationForm
    template_name = "patients/update_patient.html"
    success_url = "/patients/"

class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patients/detail_patient.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_date = datetime.now().date()
        visit_scheduels = VisitSchedule.objects.filter(patient=self.object, deleted=False)

        last_visit = visit_scheduels.filter(date__lte=curr_date).order_by('-date').first()
        next_visit = visit_scheduels.filter(date__gt=curr_date).order_by('date').first()
        
        context['last_visit'] = f"{last_visit.date.strftime('%d %b %Y')} @ {last_visit.time.strftime('%I %p')}" if last_visit else "Not visited yet"
        context['next_visit'] = f"{next_visit.date.strftime('%d %b %Y')} @ {next_visit.time.strftime('%I %p')}" if next_visit else "No visit scheduled"
        return context

class PatientFamilyListView(LoginRequiredMixin, ListView):
    model = PatientFamily
    context_object_name = 'patient_families'
    template_name = "patients/patient_family.html"

    def get_queryset(self):
        patient_id = self.kwargs['uid']
        return PatientFamily.objects.filter(patient__id=patient_id, deleted=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['uid'])
        return context


class PatientFamilyCreateView(AuthorisedPatientManager, CreateView):
    permission_required = "patients.add_patientfamily"
    model = PatientFamily
    form_class = PatientFamilyCreationForm
    template_name = "patients/create_patient_family.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        patient_id = self.kwargs['uid']
        self.object.patient = Patient.objects.get(pk=patient_id)
        self.object.save()

        return HttpResponseRedirect(f"/patients/{patient_id}/family")

class PatientFamilyUpdateView(AuthorisedPatientManager, UpdateView):
    permission_required = "patients.change_patientfamily"
    model = PatientFamily
    form_class = PatientFamilyCreationForm
    template_name = "patients/update_patient_family.html"
    
    def form_valid(self, form):
        self.object = form.save()
        patient_id = self.kwargs['uid']

        return HttpResponseRedirect(f"/patients/{patient_id}/family")

class PatientFamilyDeleteView(AuthorisedPatientManager, DeleteView):
    permission_required = "patients.delete_patientfamily"
    model = PatientFamily
    template_name = "patients/delete_patient_family.html"
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        PatientFamily.objects.filter(pk=self.object.pk).update(deleted=True)
        patient_id = kwargs['uid']

        return HttpResponseRedirect(f"/patients/{patient_id}/family")

class PatientVisitHistoryView(LoginRequiredMixin, ListView):
    model = VisitSchedule
    context_object_name = "visit_histories"
    template_name = "patients/visit_history.html"

    def get_queryset(self):
        patient_id = self.kwargs['uid']
        curr_date = datetime.now().date()
        return VisitSchedule.objects.filter(patient__id=patient_id, deleted=False, date__lt=curr_date)


class PatientVisitHistoryDetailView(LoginRequiredMixin, DetailView):
    template_name = "patients/visit_details.html"
    
    def get_object(self):
        return VisitDetail.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = TreatmentNote.objects.filter(visit_details__id=self.kwargs['pk'])
        return context 

