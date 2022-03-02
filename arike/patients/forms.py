from django.forms import ModelForm
from arike.patients.models import Patient

class PatientCreationForm(ModelForm):

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'phone_number', 'emergency_phone_number', 'address', 'ward', 'facility', 'gender']
    
    def __init__(self, *args, **kwargs):
        super(PatientCreationForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].required = False 
        self.fields['emergency_phone_number'].required = False
