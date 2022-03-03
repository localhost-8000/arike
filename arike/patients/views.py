from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from arike.patients.forms import PatientCreationForm, PatientFamilyCreationForm

from arike.patients.models import Patient, PatientFamily


class PatientsListView(ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'patients/patients.html'

    def get_queryset(self):
        return Patient.objects.all()


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = "patients/create_patient.html"
    success_url = "/patients/"

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = "patients/update_patient.html"
    success_url = "/patients/"

class PatientDetailView(DetailView):
    model = Patient
    template_name = "patients/detail_patient.html"

class PatientFamilyListView(ListView):
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


class PatientFamilyCreateView(CreateView):
    model = PatientFamily
    form_class = PatientFamilyCreationForm
    template_name = "patients/create_patient_family.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        patient_id = self.kwargs['uid']
        self.object.patient = Patient.objects.get(pk=patient_id)
        self.object.save()

        return HttpResponseRedirect(f"/patients/{patient_id}/family")

class PatientFamilyUpdateView(UpdateView):
    model = PatientFamily
    form_class = PatientFamilyCreationForm
    template_name = "patients/update_patient_family.html"
    
    def form_valid(self, form):
        self.object = form.save()
        patient_id = self.kwargs['uid']

        return HttpResponseRedirect(f"/patients/{patient_id}/family")

class PatientFamilyDeleteView(DeleteView):
    model = PatientFamily
    template_name = "patients/delete_patient_family.html"
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        PatientFamily.objects.filter(pk=self.object.pk).update(deleted=True)
        patient_id = kwargs['uid']

        return HttpResponseRedirect(f"/patients/{patient_id}/family")