from django.contrib import admin

from arike.treatments.models import (
    CareSubType,
    CareType,
    Disease,
    PatientDisease,
    Treatment,
    TreatmentNote,
)

admin.site.register(Disease)
admin.site.register(Treatment)
admin.site.register(TreatmentNote)
admin.site.register(PatientDisease)
admin.site.register(CareType)
admin.site.register(CareSubType)
