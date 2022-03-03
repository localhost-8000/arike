from django.contrib.auth import get_user_model
from django.db import models

from arike.patients.models import Patient

User = get_user_model()

class VisitSchedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VisitDetails(models.Model):
    palliative_phase = models.CharField(max_length=50)
    blood_pressure = models.CharField(max_length=50)
    pulse = models.CharField(max_length=50)
    general_random_blood_sugar = models.CharField(max_length=50)
    personal_hygiene = models.CharField(max_length=50)
    mouth_hygiene = models.CharField(max_length=50)
    public_hygiene = models.CharField(max_length=50)
    systemic_examination = models.CharField(max_length=50)
    patient_at_peace = models.BooleanField(default=False)
    pain = models.BooleanField(default=True)
    symptoms = models.CharField(max_length=200)
    note = models.CharField(max_length=400)
    visit_schedule = models.ForeignKey(VisitSchedule, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
