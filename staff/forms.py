from django import forms
from .models import StaffModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from services.models import Service
from easy_select2 import *

class StaffModelForm(UserCreationForm):
    required_css_class = 'required'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(StaffModelForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_staff = 1
        # user.groups = 'Staff'

        user.save()
        return user

class ExtendedStaffModelForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), widget=forms.SelectMultiple)

    class Meta:
        model = StaffModel
        fields = ('phone_number', 'services')

class StaffUpdateForm(forms.ModelForm):
        # services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), widget=forms.SelectMultiple, help_text = "Choose multiple.")
        services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(),widget=Select2Multiple(
        select2attrs={'width': 'auto'}))
        is_active = forms.BooleanField(widget=forms.CheckboxInput, required=False)

        class Meta:
            model = StaffModel
            fields = ('about', 'phone_number', 'services','is_active')
