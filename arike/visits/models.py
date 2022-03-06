from django.contrib.auth import get_user_model
from django.db import models

from arike.patients.models import Patient

User = get_user_model()

PALLIATIVE_PHASE_CHOICES = (
    ('1', 'Stable'),
    ('2', 'Unstable'),
    ('3', 'Deteriorating'),
    ('4', 'Dying'),
)

SYSTEMIC_EXAMINATION_CHOICES = (
    ('1', 'Cardiovascular'),
    ('2', 'Central nervous system'),
    ('3', 'Gastrointestinal'),
    ('4', 'Genital-urinary'),
    ('5', 'Respiratory'),
)

BOOL_CHOICES = (
    (True, 'Yes'),
    (False, 'No'),
)

class VisitSchedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class VisitDetail(models.Model):
    palliative_phase = models.CharField(max_length=50, choices=PALLIATIVE_PHASE_CHOICES)
    blood_pressure = models.CharField(max_length=50)
    pulse = models.CharField(max_length=50)
    general_random_blood_sugar = models.CharField(max_length=50)
    personal_hygiene = models.CharField(max_length=50)
    mouth_hygiene = models.CharField(max_length=50)
    public_hygiene = models.CharField(max_length=50)
    systemic_examination = models.CharField(max_length=50, choices=SYSTEMIC_EXAMINATION_CHOICES)
    patient_at_peace = models.BooleanField(choices=BOOL_CHOICES, default=False)
    pain = models.BooleanField(default=True)
    symptoms = models.CharField(max_length=200)
    note = models.CharField(max_length=400)
    visit_schedule = models.ForeignKey(VisitSchedule, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
