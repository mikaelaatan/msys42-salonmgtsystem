from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
from .forms import ServiceCreateForm

# def addnewservice_view(request):
#     form = ServiceCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, 'addservice.html',context)


def addservice_view(request):
    form = ServiceCreateForm()
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'addservice.html',context)

# Create your views here.
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
