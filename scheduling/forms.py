from django import forms
from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from staff.models import StaffModel
from customers.models import Customer
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    required_css_class = 'required'
    services = forms.ModelMultipleChoiceField(Service.objects.all(), widget=forms.CheckboxSelectMultiple)
    staffs = forms.ModelChoiceField(StaffModel.objects.all(), widget=forms.RadioSelect)

    class Meta:
        model = Appointment
        fields = ('appointmentdate', 'appointmenttime', 'iscancelled', 'customers','staffs', 'services')

class AppointmentReviewForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('avg_rating', 'comment')
