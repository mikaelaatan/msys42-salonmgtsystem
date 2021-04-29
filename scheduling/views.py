from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import AppointmentForm
from django.views.generic import *
from django.urls import reverse

from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar

# Create your views here.


################### CALENDAR #################
def index(request):
    return HttpResponse('hello')

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
class AppointmentCreateView(CreateView):
    template_name = 'createbooking.html'
    form_class = AppointmentForm
    queryset = Appointment.objects.all()

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'appointmentlist.html'
    queryset = Appointment.objects.all()

# def home(request):
#     return render(request, 'about.html',{})
#
# def book(request):
#     staff = StaffModel.objects.values_list('name',flat=True)
#     services_ = Service.objects.values_list('name',flat=True)
#     services = []
#     for i in services_:
#         staff.append(i)
#     context = {
#         'staff':staff,
#         'services':services,
#     }
#     return render(request,'book.html',context=context)
#
# def appointment(request):
#     if request.method=='POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         service = request.POST.get('service')
#         contact = request.POST.get('contact')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         note = request.POST.get('note')
#
#         obj = Appointment.objects.create(name=name,email=email,service=service,contact=contact,date=date,time=time,note=note)
#
#         return redirect('home')
#     return redirect('home')
#
# def success(request):
#     print(request.POST)
#     order_id = random_string_generator()
#     email = request.POST.get('email')
#     service = request.POST.get('service')
#     date = request.POST.get('date')
#     time = request.POST.get('time')
#     stylist = request.POST.get('employee')
#     if stylist == 'Random Stylist':
#         stylists = Employee.objects.values_list('name', flat=True)
#         print(stylists)
#         stylist = random.choice(stylists)
#     name  = request.POST.get('name')
#     obj = Service.objects.filter(name=service).first()
#     try:
#         amount = obj.price
#     except:
#         amount = "N/A"
#     context = {
#         'email':email,
#         'name':name,
#         'service':service,
#         'stylist':stylist,
#         'date':date,
#         'time':time,
#         'order_id':order_id,
#         'contact':contact,
#         'amount':amount,
#     }
#     return render(request,'success.html',context=context)
