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
    staff = forms.ModelChoiceField(StaffModel.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = Appointment
        fields = ('appdatetime', 'customer','staff', 'service')
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
         }

    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M',)

class UpdateAppointmentForm(forms.ModelForm):
    required_css_class = 'required'
    service = forms.ModelChoiceField(Service.objects.all(), widget=forms.Select)
    staff = forms.ModelChoiceField(StaffModel.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = Appointment
        fields = ('appdatetime', 'iscancelled','staff', 'service')
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
         }

    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M',)

#
# class AppointmentReviewForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ('avg_rating', 'comment')
