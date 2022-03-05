from django.contrib import admin
from arike.patients.models import Patient, PatientFamily

admin.site.register(Patient)
admin.site.register(PatientFamily)