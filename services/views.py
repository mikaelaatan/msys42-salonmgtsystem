from django.shortcuts import render

# Create your views here.
def services_view (request,  *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello World</h1>")
