
from django.contrib.auth import get_user_model, forms
from django.forms import ModelChoiceField, ModelForm
from django.utils.translation import gettext_lazy as _

from arike.home.models import District

User = get_user_model()


class UserCreateForm(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "district"]
    
    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        if len(data) < 2:
            self.add_error("first_name", "First name must be at least 2 characters long")
        return data
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        if not data:
            self.add_error("email", "Email is required")
        return data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["district"] = ModelChoiceField(queryset=District.objects.all(), empty_label=None)

class UserFacilityAssignForm(ModelForm):

    class Meta:
        model = User 
        fields = ["facility", "role"]

    def clean_facility(self):
        data = self.cleaned_data["facility"]
        if not data:
            self.add_error("facility", "Facility is required")
        return data

    def clean_role(self):
        data = self.cleaned_data["role"]
        if not data or data == "none":
            self.add_error("role", "Role is required")
        return data
