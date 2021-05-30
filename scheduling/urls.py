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
from django.urls import path
from . import views
from django.conf.urls import url
from .views import *

app_name = 'scheduling'
urlpatterns = [
    path('admin/new/', admin_appointment_book_view, name='admin-appointment-new'),
    path('new/', appointment_book_view, name='appointment-new'),
    path('', appointment_view, name='appointment-list'),
    path('<int:id>/', views.dynamic_lookup_view, name='booking-details'),
    path('edit/<int:id>/', edit_appointment_view, name='appointment-edit'),
    path('admin/edit/<int:id>/', admin_edit_appointment_view, name='admin-appointment-edit'),
    path('ajax/load-staff/', views.load_staff, name='ajax_load_staff'),
    # path('ajax/load-time/', views.load_endtime, name='ajax_load_time'),
    path('calendar/', appointment_calendar_view, name='appointment-calendar'),
]
