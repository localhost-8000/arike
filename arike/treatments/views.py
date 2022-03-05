
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from arike.patients.models import Patient
from arike.treatments.forms import DiseaseHistoryCreationForm, TreatmentCreationForm
from arike.treatments.models import CareSubType, PatientDisease, Treatment


class AuthorisedDiseaseHistoryManager(LoginRequiredMixin, PermissionRequiredMixin):
    def get_queryset(self):
        return PatientDisease.objects.filter(deleted=False)

class DiseaseHistoryListView(LoginRequiredMixin, ListView):
    model = PatientDisease
    context_object_name = 'disease_histories'
    template_name = "treatments/disease_history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['uid'])
        return context
    
    def get_queryset(self):
        return PatientDisease.objects.filter(patient=self.kwargs['uid'], deleted=False)

class DiseaseHistoryCreateView(AuthorisedDiseaseHistoryManager, CreateView):
    permission_required = "treatments.add_patientdisease"
    form_class = DiseaseHistoryCreationForm
    template_name = "treatments/disease_history_create.html"

    def get_success_url(self):
        return f"/patients/{self.kwargs['uid']}/disease/history"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.patient = Patient.objects.get(pk=self.kwargs['uid'])
        self.object.investigated_by = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class DiseaseHistoryUpdateView(AuthorisedDiseaseHistoryManager, UpdateView):
    permission_required = "treatments.change_patientdisease"
    model = PatientDisease
    form_class = DiseaseHistoryCreationForm
    template_name = "treatments/disease_history_update.html"

    def get_queryset(self):
        return PatientDisease.objects.filter(pk=self.kwargs['pk'])
    
    def get_success_url(self):
        return f"/patients/{self.kwargs['uid']}/disease/history"

class DiseaseHistoryDeleteView(AuthorisedDiseaseHistoryManager, DeleteView):
    permission_required = "treatments.delete_patientdisease"
    template_name = "treatments/delete_disease_history.html"

    def get_queryset(self):
        return PatientDisease.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return f"/patients/{self.kwargs['uid']}/disease/history"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        PatientDisease.objects.filter(pk=self.object.pk).update(deleted=True)

        return HttpResponseRedirect(self.get_success_url())


class TreatmentListView(LoginRequiredMixin, ListView):
    model = Treatment
    context_object_name = "treatments"
    template_name = "treatments/treatment_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs['uid'])
        return context
    
    def get_queryset(self):
        return Treatment.objects.filter(patient=self.kwargs['uid'], deleted=False)


def load_treatment_care_sub_type(request):
    care_type = request.GET.get('care_type')
    care_sub_types = CareSubType.objects.filter(care_type=care_type).order_by('name')
    return render(request, "treatments/care_sub_type_dropdown.html", {'care_sub_types': care_sub_types})

class TreatmentCreateView(AuthorisedDiseaseHistoryManager, CreateView):
    permission_required = "treatments.add_treatment"
    form_class = TreatmentCreationForm
    template_name = "treatments/create_treatment.html"

    def get_success_url(self):
        return f"/patients/{self.kwargs['uid']}/disease/treatments"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.patient = Patient.objects.get(pk=self.kwargs['uid'])
        self.object.given_by = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
    

class TreatmentUpdateView(AuthorisedDiseaseHistoryManager, UpdateView):
    permission_required = "treatments.change_treatment"
    form_class = TreatmentCreationForm
    template_name = "treatments/update_treatment.html"

    def get_queryset(self):
        return Treatment.objects.filter(pk=self.kwargs['pk'], deleted=False)
    
    def get_success_url(self):
        return f"/patients/{self.kwargs['uid']}/disease/treatments"

class TreatmentDeleteView(AuthorisedDiseaseHistoryManager, DeleteView):
    permission_required = "treatments.delete_treatment"
    template_name = "treatments/delete_treatment.html"

    def get_queryset(self):
        return Treatment.objects.filter(pk=self.kwargs['pk'], deleted=False)

    def get_success_url(self):
        return f"/patients/{self.kwargs['uid']}/disease/treatments"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        Treatment.objects.filter(pk=self.object.pk).update(deleted=True)

        return HttpResponseRedirect(self.get_success_url())


