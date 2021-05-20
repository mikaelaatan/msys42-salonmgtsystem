from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import CreateAppointmentForm, UpdateAppointmentForm
from django.views.generic import *
from django.urls import reverse
from datetime import datetime, timedelta

from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

# Create your views here.


def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Appointment, id=id)
    context = {
        "object": obj
    }
    return render(request, "booking_details.html", context)

class AppointmentCreateView(CreateView):
    template_name = 'createbooking.html'
    form_class = CreateAppointmentForm
    queryset = Appointment.objects.all()

class AppointmentUpdateView(UpdateView):
    template_name = 'createbooking.html'
    form_class = UpdateAppointmentForm
    queryset = Appointment.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Appointment, id=id_)

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointmentlist.html'
    queryset = Appointment.objects.all()
