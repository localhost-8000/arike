from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from arike.facilities.models import Facility
from arike.home.models import District

ROLE_TYPE = (
    ('none', 'None'),
    ('district_admin', 'District Admin'),
    ('primary_nurse', 'Primary Nurse'),
    ('secondary_nurse', 'Secondary Nurse'),
)

class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=14, null=True)
    role = models.CharField(max_length=30, choices=ROLE_TYPE, default=ROLE_TYPE[0][0])
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = ["email", "first_name"]

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username}) 

    def pretty_role(self):
        if self.role == 'none':
            return 'None'
        role = self.role.split('_')  
        role[0] = role[0].title()
        role[1] = role[1].title()
        return ' '.join(role)