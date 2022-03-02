from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from arike.patients.forms import PatientCreationForm

from arike.patients.models import Patient


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

class PatientDeleteView(DeleteView):
    pass