from django.forms import ModelForm 
from arike.treatments.models import CareSubType, PatientDisease, Treatment

class DiseaseHistoryCreationForm(ModelForm):

    class Meta:
        model = PatientDisease
        fields = ['disease', 'treatment', 'remarks']
    
    def clean_disease(self):
        disease = self.cleaned_data['disease']
        if disease is None:
            self.add_error('disease', 'Disease is required')
        return disease


class TreatmentCreationForm(ModelForm):

    class Meta:
        model = Treatment
        fields = ['care_type', 'care_sub_type', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['care_sub_type'].queryset = CareSubType.objects.none()

        if 'care_type' in self.data:
            try:
                care_type = int(self.data.get('care_type'))
                self.fields['care_sub_type'].queryset = CareSubType.objects.filter(care_type=care_type).order_by('name')
            except (ValueError, TypeError):
                pass 
        elif self.instance.pk:
            self.fields['care_sub_type'].queryset = CareSubType.objects.filter(care_type=self.instance.care_type).order_by('name')
    
    def clean_care_type(self):
        care_type = self.cleaned_data['care_type']
        if care_type is None:
            self.add_error('care_type', 'Care Type is required')
        return care_type
    
    def clean_care_sub_type(self):
        care_sub_type = self.cleaned_data['care_sub_type']
        if care_sub_type is None:
            self.add_error('care_sub_type', 'Care Sub Type is required')
        return care_sub_type
