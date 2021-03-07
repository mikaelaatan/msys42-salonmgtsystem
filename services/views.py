from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service
from .forms import ServiceForm

def addservice_view(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ServiceForm()
    return render(request, 'addservice.html',{'form': form})

def serviceslist_view(request):
    obj = Service.objects.all()
    print(obj)
    context = {
        'serviceobj': obj
    }
    return render(request, 'serviceslist.html',context)

def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Service, id=id)
    context = {
        "object": obj
    }
    return render(request, "service_detail.html", context)
