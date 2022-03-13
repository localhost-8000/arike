
from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from arike.facilities.models import Facility


class FacilityFilter(FilterSet):
    search = CharFilter(method="search_filter")

    class Meta:
        model = Facility
        fields = ['kind', 'ward']
    
    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) | Q(address__icontains=value)
        )
