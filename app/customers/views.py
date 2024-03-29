from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CustomerProfileForm, ExtendedCustomerProfileForm
from .models import Customer
from django.contrib import messages

# Create your views here.
def signup_view(request):
    customer_profile_form = CustomerProfileForm(request.POST or None, request.FILES or None)
    extended_customer_profile_form = ExtendedCustomerProfileForm(request.POST or None, request.FILES or None)
    valid = customer_profile_form.is_valid() * extended_customer_profile_form.is_valid()
    if valid:
        customer = customer_profile_form.save()
        # group = Group.objects.get(name='Customer')
        # customer.groups.add(group)
        extended_customer, created = Customer.objects.get_or_create(user=customer)
        for field in ['birthdate', 'phone_number']:
            setattr(extended_customer, field, extended_customer_profile_form.cleaned_data.get(field))
        extended_customer.save()
        messages.info(request, 'Account successfully created!')
        return redirect('/appointments')
    context = {
        'profile_form': customer_profile_form,
        'extended_profile_form': extended_customer_profile_form,
    }
    return render(request, 'registration/register.html', context)

# def dynamic_lookup_view(request,id):
#     obj = get_object_or_404(Customer, id=request.user.id)
#     context = {
#         "object": obj
#     }
#     return render(request, "customer_profile.html", context)
