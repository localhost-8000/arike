
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from arike.facilities.filters import FacilityFilter

from arike.facilities.forms import FacilityCreateForm
from arike.facilities.models import Facility


class AuthorisedFacilityManager(LoginRequiredMixin, PermissionRequiredMixin):

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)
    
class GenericFacilitiesView(LoginRequiredMixin, ListView):
    template_name = "facilities/facilities.html"
    context_object_name = "facilities"

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = FacilityFilter(self.request.GET, queryset=self.get_queryset())
        return context 

class GenericFacilityCreateView(AuthorisedFacilityManager, CreateView):
    permission_required = "facilities.add_facility"
    form_class = FacilityCreateForm
    template_name = "facilities/create_facility.html"
    success_url = "/facilities/"

class GenericFacilityUpdateView(AuthorisedFacilityManager, UpdateView):
    permission_required = "facilities.change_facility"
    model = Facility
    form_class = FacilityCreateForm
    template_name = "facilities/update_facility.html"
    success_url = "/facilities/"

class GenericFacilityDetailView(LoginRequiredMixin, DetailView):
    model = Facility
    template_name = "facilities/detail_facility.html"

class GenericFacilityDeleteView(AuthorisedFacilityManager, DeleteView):
    permission_required = "facilities.delete_facility"
    model = Facility
    template_name = "facilities/delete_facility.html"
    success_url = "/facilities/"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        Facility.objects.filter(pk=self.object.pk).update(deleted=True)
        return HttpResponseRedirect(self.get_success_url())
