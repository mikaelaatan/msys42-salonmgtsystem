from django import forms
from django.db import models
from django.forms import ModelForm, DateInput
from datetime import datetime, timedelta
from services.models import Service
from staff.models import StaffModel
from customers.models import Customer
from .models import Appointment


class CreateAppointmentForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Appointment
        fields = ('appdatetime','service','staff')
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
         }

    def __init__(self, *args, **kwargs):
        super(CreateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['service'].queryset = Service.objects.filter(is_working=True).order_by('servicetype')
        self.fields['staff'].queryset = StaffModel.objects.none()

        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['staff'].queryset =StaffModel.objects.filter(service=service_id).filter(is_active=True).order_by('id')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty staff queryset
        elif self.instance.pk:
            self.fields['staff'].queryset = self.instance.service.staff_set.order_by('name')

class AdminCreateAppointmentForm(forms.ModelForm):
    required_css_class = 'required'

    # service = forms.ModelChoiceField(Service.objects.all(), widget=forms.Select)
    # staff = forms.ModelChoiceField(StaffModel.objects.filter(service=service), widget=forms.Select)
    customer = forms.ModelChoiceField(Customer.objects.all(), widget=forms.Select)

    class Meta:
        model = Appointment
        fields = ('customer','appdatetime','service','staff','enddatetime',)
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
          'enddatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
          'service': forms.Select,
         }

    def __init__(self, *args, **kwargs):
        super(AdminCreateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M')
        self.fields['enddatetime'].input_formats = ('%Y-%m-%dT%H:%M')
        self.fields['service'].queryset = Service.objects.filter(is_working=True).order_by('servicetype')
        self.fields['staff'].queryset = StaffModel.objects.none()


        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                self.fields['staff'].queryset =StaffModel.objects.filter(service=service_id).filter(is_active=True).order_by('id')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty staff queryset
        elif self.instance.pk:
            self.fields['staff'].queryset = self.instance.service.staff_set.order_by('name')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     date = cleaned_data.get('appdatetime')
    #     staff = cleaned_data.get('staff')
    #     service = cleaned_data.get('service')
    #     if date and staff:
    #         if date.replace(tzinfo=None) < datetime.today():
    #             raise forms.ValidationError('Cannot pick a recent date for future appointment')
    #         booked_dates = Appointment.objects.filter(staff=staff, iscancelled=False).values_list('date', flat=True)
    #         for booked_date in booked_dates:
    #             length = service.objects.serviceduration
    #             if date >= booked_date and date < booked_date + length:
    #                 raise forms.ValidationError('This date is already booked for this staff member')

    # def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
    #     overlap = False
    #     if new_start == fixed_end or new_end == fixed_start:    #edge case
    #         overlap = False
    #     elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
    #         overlap = True
    #     elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
    #         overlap = True
    #     return overlap


class UpdateAppointmentForm(forms.ModelForm):
    required_css_class = 'required'

    service = forms.ModelChoiceField(Service.objects.all(), widget=forms.Select)

    class Meta:
        model = Appointment
        fields = ('appdatetime','service','staff', 'iscancelled')
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
        fields = ('customer','appdatetime','service','staff','iscancelled')
        widgets = {
          'appdatetime': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
         }

    def __init__(self, *args, **kwargs):
        super(AdminUpdateAppointmentForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields['appdatetime'].input_formats = ('%Y-%m-%dT%H:%M',)


# class AppointmentReviewForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ('avg_rating', 'comment')
