from .models import Appointment
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import AppointmentForm
from django.views.generic import *
from django.urls import reverse

# Create your views here.

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
