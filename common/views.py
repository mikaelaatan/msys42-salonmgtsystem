from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from customers.models import Customer
from services.models import Service
from staff.models import StaffModel
from scheduling.models import Appointment

# Create your views here.
def unauthorized_view(request):
    return render(request, 'unauthorized.html')

def login_required_view(request):
    return render(request, 'login_required.html')

@login_required
def home_view(request):
    if hasattr(request.user, 'staff'):
        appointments = Appointment.objects.filter(staff__user=request.user)
        services=Service.objects.filter(is_working=True)
        staffs=StaffModel.objects.all()
    elif hasattr(request.user, 'user'):
        appointments = Appointment.objects.filter(customer__user=request.user)
        services=Service.objects.all().filter(is_working=True)
        staffs=StaffModel.objects.all().filter(is_active=True)
    else:
        appointments=Appointment.objects.all()
        services=Service.objects.all()
        staffs=StaffModel.objects.all()
    appointments_today = appointments.order_by('appdatetime')
    context = {
        'todays': appointments_today,
        "services": services,
        "staffs": staffs,
    }
    return render(request, 'overview.html', context)
