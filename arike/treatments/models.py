from django.db import models

from arike.patients.models import Patient
from arike.visits.models import VisitDetails


class Disease(models.Model):
    name = models.CharField(max_length=100)
    icds_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class Treatment(models.Model):
    description = models.CharField(max_length=300)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TreatmentNote(models.Model):
    note = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    visit_details = models.ForeignKey(VisitDetails, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PatientDisease(models.Model):
    note = models.CharField(max_length=200, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
