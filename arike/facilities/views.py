
from django import forms
from django.forms import ModelForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect

from arike.facilities.models import Facility, Ward, FACILITY_KIND_CHOICES


class FacilityCreateForm(ModelForm):
    kind = forms.ChoiceField(choices=FACILITY_KIND_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Facility
        fields = ['name', 'address', 'ward', 'pin_code', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(FacilityCreateForm, self).__init__(*args, **kwargs)
        self.fields['ward'] = forms.ModelChoiceField(queryset=Ward.objects.all())

class GenericFacilitiesView(ListView):
    template_name = "facilities/facilities.html"
    context_object_name = "facilities"

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)

class GenericFacilityCreateView(CreateView):
    form_class = FacilityCreateForm
    template_name = "facilities/create_facility.html"
    success_url = "/facilities/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.kind = form.cleaned_data['kind']
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class GenericFacilityUpdateView(UpdateView):
    model = Facility
    form_class = FacilityCreateForm
    template_name = "facilities/update_facility.html"
    succss_url = "/facilities/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.kind = form.cleaned_data['kind']
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class GenericFacilityDetailView(DetailView):
    model = Facility
    template_name = "facilities/detail_facility.html"

class GenericFacilityDeleteView(DeleteView):
    model = Facility
    template_name = "facilities/delete_facility.html"
    success_url = "/facilities/"

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        Facility.objects.filter(pk=self.object.pk).update(deleted=True)
        return HttpResponseRedirect(self.get_success_url())