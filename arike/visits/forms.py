
from django import forms
from django.forms import ModelForm
from arike.treatments.models import TreatmentNote 
from arike.visits.models import VisitSchedule, VisitDetail

class VisitScheduleForm(ModelForm):

    class Meta:
        model = VisitSchedule
        fields = ["date", "time", "duration"]
        labels = {
            "date": "Date of Visit",
            "time": "Time of Visit",
            "duration": "Duration (minutes)"
        }

class VisitDetailCreationForm(ModelForm):

    class Meta:
        model = VisitDetail
        fields = "__all__"
        exclude = ["visit_schedule", "public_hygiene", "pain", "symptoms", "created_at", "updated_at"]
        widget = {
            "patient_at_peace": forms.RadioSelect
        }


class TreatmentNoteCreationForm(ModelForm):

    class Meta:
        model = TreatmentNote
        fields = ["note"]