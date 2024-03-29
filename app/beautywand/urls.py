"""beautywand URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import *

from scheduling import views
from services import views
from staff import views

# ----- no sidebar admin page ---------
admin.autodiscover()
admin.site.enable_nav_sidebar = False
# -------------------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include('scheduling.urls')),
    path('services/', include('services.urls')),
    path('staff/', include('staff.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('customers.urls')),
    path('', include('Calendar.urls')),
    path('', include('common.urls')),
]
