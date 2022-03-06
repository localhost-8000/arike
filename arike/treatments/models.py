from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from arike.patients.models import Patient
from arike.visits.models import User, VisitDetail

User = get_user_model()

class Disease(models.Model):
    name = models.CharField(max_length=100)
    icds_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 

class CareType(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class CareSubType(models.Model):
    name = models.CharField(max_length=200)
    care_type = models.ForeignKey(CareType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Treatment(models.Model):
    care_type = models.ForeignKey(CareType, on_delete=models.CASCADE)
    care_sub_type = models.ForeignKey(CareSubType, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    given_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def pretty_created_date(self):
        return self.created_at.strftime("%d %b %Y")
    
    def pretty_updated_date(self):
        return self.updated_at.strftime("%d %b %Y")

class TreatmentNote(models.Model):
    note = models.CharField(max_length=200)
    description = models.CharField(max_length=300, null=True, blank=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    visit_details = models.ForeignKey(VisitDetail, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note

    def pretty_created_date(self):
        return self.created_at.strftime("%d %b %Y")

class PatientDisease(models.Model):
    remarks = models.CharField(max_length=200, blank=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, blank=True, null=True)
    investigated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def pretty_updated(self):
        return self.updated_at.strftime("%d %b %Y")
