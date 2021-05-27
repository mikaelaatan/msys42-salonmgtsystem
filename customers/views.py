from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomerProfileForm, ExtendedCustomerProfileForm
from .models import Customer

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def signup_view(request):
    customer_profile_form = CustomerProfileForm(request.POST or None, request.FILES or None)
    extended_customer_profile_form = ExtendedCustomerProfileForm(request.POST or None, request.FILES or None)
    valid = customer_profile_form.is_valid() * extended_customer_profile_form.is_valid()
    if valid:
        customer = customer_profile_form.save()
        group = Group.objects.get(name='Customer')
        customer.groups.add(group)
        extended_customer, created = Customer.objects.get_or_create(user=customer)
        for field in ['birthdate', 'phone_number']:
            setattr(extended_customer, field, extended_customer_profile_form.cleaned_data.get(field))
        extended_customer.save()
        return redirect('/appointments')
    context = {
        'profile_form': customer_profile_form,
        'extended_profile_form': extended_customer_profile_form,
    }
    return render(request, 'registration/login.html', context)
