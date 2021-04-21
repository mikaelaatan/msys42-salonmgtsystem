from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def employees_list(request):
    return render(request, 'employeeslist.html',{})


# def dynamic_lookup_view(request,id):
#     obj = get_object_or_404(Service, id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "service_detail.html", context)