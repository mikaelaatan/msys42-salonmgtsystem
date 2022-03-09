from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service
from .forms import ServiceForm
from django.views.generic import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from decorators import user_required, staff_required, admin_required
from django.utils.decorators import method_decorator

# DETAILED VIEW
def dynamic_lookup_view(request,id):
    obj = get_object_or_404(Service, id=id)
    context = {
        "object": obj
    }
    return render(request, "service_detail.html", context)

# class ServiceListView(ListView):
#     model = Service
#     template_name = 'serviceslist.html'
#     queryset = Service.objects.all()

def servicelist_view(request):
    if hasattr(request.user, 'user'):
        services = Service.objects.filter(is_working=True)
    else:
        services = Service.objects.all()
    service_now = services.order_by('servicetype')
    context = {
        'object_list': service_now,
    }
    return render(request, 'service_list.html', context)

@method_decorator(admin_required, name='dispatch')
class ServiceCreateView(CreateView):
    template_name = 'addservice.html'
    form_class = ServiceForm
    queryset = Service.objects.all()

@method_decorator(admin_required, name='dispatch')
class ServiceUpdateView(UpdateView):
    template_name = 'addservice.html'
    form_class = ServiceForm
    queryset = Service.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Service, id=id_)

@method_decorator(admin_required, name='dispatch')
class ServiceDeleteView(DeleteView):
    template_name = 'deleteservice.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Service, id=id_)

    def get_success_url(self):
        return reverse('services:service-list')

# def serviceslist_view(request):
#     obj = Service.objects.all()
#     print(obj)
#     context = {
#         'serviceobj': obj
#     }
#     return render(request, 'serviceslist.html',context)
#
#
# def addservice_view(request):
#     form = ServiceForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ServiceForm()
#     return render(request, 'addservice.html',{'form': form})
