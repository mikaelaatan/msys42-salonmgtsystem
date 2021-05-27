from django.shortcuts import render

# Create your views here.
def unauthorized_view(request):
    return render(request, 'unauthorized.html')

def login_required_view(request):
    return render(request, 'login_required.html')

def home_view(request):
    return render(request, 'home_template.html')
