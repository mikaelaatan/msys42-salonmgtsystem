from django import forms
from django.forms import ModelForm, DateInput
from .models import Customer
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
        fields = ('birthdate', 'phone_number')
        widgets = {
          'birthdate': DateInput(attrs={'type': 'date'}, format='%m/%d/%Y'),
         }

        def __init__(self, *args, **kwargs):
            super(ExtendedCustomerProfileForm, self).__init__(*args, **kwargs)
            # input_formats to parse HTML5 datetime-local input to datetime field
            self.fields['birthdate'].input_formats = ('%m/%d/%Y')
