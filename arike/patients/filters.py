
from django.db.models import Q
from django_filters.rest_framework import CharFilter, FilterSet

from .models import Patient


class PatientFilter(FilterSet):
    search = CharFilter(method="search_by_first_and_last_name")

    class Meta:
        model = Patient 
        fields = ['ward', 'facility']

    def search_by_first_and_last_name(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value)
        )
