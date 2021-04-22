from django import forms
from .models import CustomerProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomerProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(CustomerProfileForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class ExtendedCustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('city', 'country', 'birthdate', 'phone_number')
