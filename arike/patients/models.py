from datetime import datetime, date
from django.db import models

from arike.facilities.models import Facility, Ward

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

class Patient(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default=GENDER_CHOICE[0][0])
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    emergency_phone_number = models.CharField(max_length=14, null=True)
    expired_time = models.DateTimeField(null=True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def is_expired(self):
        return self.expired_time <= datetime.now()

    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

class PatientFamily(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=14)
    relation = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    occupation = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default=GENDER_CHOICE[0][0])
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
