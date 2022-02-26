from django.db import models
from arike.home.models import LsgBody

FACILITY_KIND_CHOICES = (
    ('phc', 'PHC'),
    ('chc', 'CHC'),
)

class Ward(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    lsg_body = models.ForeignKey(LsgBody, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Facility(models.Model):
    kind = models.CharField(max_length=100, choices=FACILITY_KIND_CHOICES, default=FACILITY_KIND_CHOICES[0][0])
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pin_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=14)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    def pretty_kind(self):
        return self.kind.upper()

