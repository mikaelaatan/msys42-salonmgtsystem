from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime, date, timedelta
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.safestring import mark_safe
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm

# Create your views here.

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'Calendar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('month', None))

        #Instantiate our calendar class with today's year & date
        cal = Calendar(d.year, d.month)

        #Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear = True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day = 1)
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
    
def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
        
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('Calendar:calendar'))
    return render(request, 'Calendar/event.html', {'form': form})

def create_event(request):    
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        servicename = form.cleaned_data['servicename']
        clientname = form.cleaned_data['clientname']
        staffname = form.cleaned_data['staffname']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            servicename=servicename,
            clientname=clientname,
            staffname=staffname,
            start_time=start_time,
            end_time=end_time
        )
        return HttpResponseRedirect(reverse('Calendar:calendar'))
    return render(request, 'event.html', {'form': form})

class EventEdit(generic.UpdateView):
    model = Event
    fields = ['servicename', 'clientname', 'staffname', 'start_time', 'end_time']
    template_name = 'event1.html'

def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
        'eventmember': eventmember
    }
    return render(request, 'event-details.html', context)

class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = 'event-delete.html'
    success_url = reverse_lazy('Calendar:calendar')