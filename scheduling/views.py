from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.views.generic import *
from django.urls import reverse
from django.db import transaction
from datetime import date, timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from decorators import user_required, staff_required, admin_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from customers.models import Customer
from services.models import Service
from staff.models import StaffModel
from .models import *
from datetime import datetime, date

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib import messages

# Create your views here.

def load_staff(request):
    service_id = request.GET.get('service')
    staffs = StaffModel.objects.filter(service=service_id).filter(is_active=True).order_by('id')
    return render(request, 'staff_dropdown_list_options.html', {'staffs': staffs})

@login_required
def appointment_view(request):
    if hasattr(request.user, 'staff'):
        appointments = Appointment.objects.filter(staff__user=request.user)
    elif hasattr(request.user, 'user'):
        appointments = Appointment.objects.filter(customer__user=request.user)
    else:
        appointments=Appointment.objects.all()
    appointments_today = appointments.order_by('appdatetime')
    context = {
        'todays': appointments_today,
    }
    return render(request, 'appointmentlist.html', context)

def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Appointment, id=id)
    context = {
        "object": obj,
    }
    return render(request, "booking_details.html", context)

@transaction.atomic
@user_required
def appointment_book_view(request):
    customer = Customer.objects.get(user=request.user)
    form = CreateAppointmentForm(
        request.POST or None,
    )
    if form.is_valid():
        appointment = form.save(commit=False)
        appointment.customer = customer
        appointment.save()
        messages.info(request, 'Appointment saved successfully!')
        return redirect('scheduling:appointment-list')
    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'createbooking.html', context)

@transaction.atomic
@admin_required
def admin_appointment_book_view(request):
    if request.method == 'POST':
        form = AdminCreateAppointmentForm(request.POST or None)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            messages.info(request, 'Appointment saved successfully!')
            return redirect('scheduling:appointment-list')
    else:
        form = AdminCreateAppointmentForm()
    context = {
        'form': form,
    }
    return render(request, 'admin_createbooking.html', context)

@method_decorator(login_required, name='dispatch')
class AppointmentUpdateView(SuccessMessageMixin,UpdateView):
    template_name = 'createbooking.html'
    form_class = UpdateAppointmentForm
    queryset = Appointment.objects.all()
    success_message = 'Appointment has been edited successfully!'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Appointment, id=id_)

    def get_context_data(self, *args, **kwargs):
        context = super(AppointmentUpdateView, self).get_context_data(*args, **kwargs)
        customer = Customer.objects.get(user=self.request.user)
        context['customer'] = customer
        print (self.request.user)
        return context

@method_decorator(admin_required, name='dispatch')
class AdminAppointmentUpdateView(SuccessMessageMixin,UpdateView):
    template_name = 'admin_createbooking.html'
    form_class = AdminUpdateAppointmentForm
    queryset = Appointment.objects.all()
    success_message = 'Appointment has been edited successfully!'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Appointment, id=id_)

def appointment_calendar_view(request):
    if hasattr(request.user, 'staff'):
        appointments = Appointment.objects.filter(iscancelled=False, staff__user=request.user)
    else:
        appointments = Appointment.objects.filter(iscancelled=False)
    today = date.today()
    context = {
        'appointments': appointments,
        'today': today,
    }
    return render(request, 'appointment_calendar.html', context)
