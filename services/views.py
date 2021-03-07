from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
from .forms import ServiceForm

def addservice_view(request):
    my_form = ServiceForm()
    if request.method == "POST":
        my_form = ServiceForm(request.POST)
        if my_form.is_valid():
            Service.objects.create(my_form.cleaned_data)
    return render(request, 'addservice.html',{'form': my_form})

def listofservices_view(request):
    obj = Service.objects.get(id=1)
    # context = {
    #     'Name': obj.servicename,
    #     'Price': obj.ServicePrice
    # }
    context = {
        'serviceobj': obj
    }
    return render(request, 'listofservices.html',context)
