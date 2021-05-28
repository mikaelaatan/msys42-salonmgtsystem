from django import forms
from django.db import models
from django.forms import ModelForm, DateInput

from services.models import Service
from staff.models import StaffModel
from customers.models import Customer
from .models import Appointment


class CreateAppointmentForm(forms.ModelForm):
    required_css_class = 'required'

    service = forms.ModelChoiceField(Service.objects.all(), widget=forms.Select)
    staff = forms.ModelChoiceField(StaffModel.objects.all(), widget=forms.Select)

    class Meta:
        model = Appointment
        fields = ('appdatetime','staff', 'service')
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
         }

    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M',)

class AdminCreateAppointmentForm(forms.ModelForm):
    required_css_class = 'required'
    # children_ids = Staff.objects.filter(name__startswith='A').values_list('child', flat=True)
    # children = Service.objects.filter(pk__in=children_ids)

    service = forms.ModelChoiceField(Service.objects.all(), widget=forms.Select)
    staff = forms.ModelChoiceField(StaffModel.objects.all(), widget=forms.Select)
    customer = forms.ModelChoiceField(Customer.objects.all(), widget=forms.Select)

    class Meta:
        model = Appointment
        fields = ('customer','appdatetime','staff', 'service')
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
         }

    def __init__(self, *args, **kwargs):
        super(AdminCreateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M',)

class UpdateAppointmentForm(forms.ModelForm):
    required_css_class = 'required'

    service = forms.ModelChoiceField(Service.objects.all(), widget=forms.Select)
    staff = forms.ModelChoiceField(StaffModel.objects.all(), widget=forms.Select)

    class Meta:
        model = Appointment
        fields = ('appdatetime','staff', 'service','iscancelled')
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
         }

    def __init__(self, *args, **kwargs):
        super(UpdateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M',)

class AdminUpdateAppointmentForm(forms.ModelForm):
    required_css_class = 'required'
    customer = forms.ModelChoiceField(Customer.objects.all(), widget=forms.Select)
    service = forms.ModelChoiceField(Service.objects.all(), widget=forms.Select)
    staff = forms.ModelChoiceField(StaffModel.objects.all(), widget=forms.Select)

    class Meta:
        model = Appointment
        fields = ('customer','appdatetime','staff', 'service','iscancelled')
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
         }

    def __init__(self, *args, **kwargs):
        super(AdminUpdateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M',)

    def save(self, commit=True):
        user = super(CustomerProfileForm, self).save(commit=True)


# class AppointmentReviewForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ('avg_rating', 'comment')
