
from django import template
from arike.facilities.models import Ward

register = template.Library()

def get_ward_name(ward_id):
    try:
        return Ward.objects.get(pk=ward_id).name
    except:
        return "" 

register.filter('ward_name', get_ward_name)