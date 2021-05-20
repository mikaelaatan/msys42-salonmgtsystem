from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
<<<<<<< HEAD
from .forms import CreateAppointmentForm, UpdateAppointmentForm
=======
from .forms import CreateAppointmentForm
>>>>>>> 08d63756320583424d9edbcd0240e4f03147dcfe
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

<<<<<<< HEAD
=======
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


class CalendarView(ListView):
    model = Appointment
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Appointment, pk=event_id)
    else:
        instance = Event()

    form = AppointmentForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('scheduling:calendar'))
    return render(request, 'createbooking.html', {'form': form})


####################################################
def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Appointment, id=id)
    context = {
        "object": obj
    }
    return render(request, "booking_details.html", context)

>>>>>>> 08d63756320583424d9edbcd0240e4f03147dcfe
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
