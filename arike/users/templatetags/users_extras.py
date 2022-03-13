from django import template
from django.template import Library

register = Library()

@register.filter(name="get_district")
def get_district_name_by_id(id):
    try:
        from arike.home.models import District
        return District.objects.get(pk=id).name
    except:
        return ""

@register.filter(name="get_facility")
def get_facility_name_by_id(id):
    try:
        from arike.facilities.models import Facility
        return Facility.objects.get(pk=id).name
    except:
        return ""

@register.filter(name="pretty_role")
def get_prettified_role(role):
    try:
        role = role.split("_")
        role = [char.capitalize() for char in role]
        return " ".join(role)
    except:
        return role 