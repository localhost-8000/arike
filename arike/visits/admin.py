from django.contrib import admin

from arike.visits.models import VisitDetail, VisitSchedule

admin.site.register(VisitSchedule)
admin.site.register(VisitDetail)