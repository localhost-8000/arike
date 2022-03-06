from django import forms
from arike.facilities.models import Facility

class FacilityCreateForm(forms.ModelForm):

    class Meta:
        model = Facility
        fields = ['kind', 'name', 'address', 'ward', 'pin_code', 'phone_number']

    def clean_name(self):
        data = self.cleaned_data['name']
        if data is None:
            self.add_error('name', 'Name is required')
        return data 

    def clean_pin_code(self):
        data = self.cleaned_data['pin_code']
        if data is None:
            self.add_error('pin_code', 'Pin code is required')
        return data 
    