from datetime import date, datetime

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

from arike.facilities.models import Facility, Ward

GENDER_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

RELATION_CHOICE = (
    ('1', 'Father'),
    ('2', 'Mother'),
    ('3', 'Son'),
    ('4', 'Sister'),
    ('5', 'GrandFather'),
    ('6', 'GrandMother'),
    ('7', 'Uncle'),
    ('8', 'Aunt'),
    ('9', 'Others'),
)

EDUCATION_CHOICE = (
    ('1', '10th Passed'),
    ('2', '12th Passed'),
    ('3', 'Graduation'),
    ('4', 'Post Graduation'),
    ('5', 'PhD'),
    ('6', 'Illiterate'),
    ('7', 'Others'),
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
    deleted = models.BooleanField(default=False)
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
    relation = models.CharField(max_length=50, choices=RELATION_CHOICE, default=RELATION_CHOICE[0][0])
    education = models.CharField(max_length=50, choices=EDUCATION_CHOICE, default=EDUCATION_CHOICE[0][0])
    occupation = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default=GENDER_CHOICE[0][0])
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age
