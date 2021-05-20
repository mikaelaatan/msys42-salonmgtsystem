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
    path('new/', AppointmentCreateView.as_view(), name='appointment-new'),
    path('', AppointmentListView.as_view(), name='appointment-list'),
    path('<int:id>/', views.dynamic_lookup_view, name='booking-details'),
<<<<<<< HEAD
    path('edit/<int:id>/', AppointmentUpdateView.as_view(), name='appointment-edit'),
=======
    # path('edit/<int:id>/', StaffUpdateView.as_view(), name='staff-edit'),
>>>>>>> 08d63756320583424d9edbcd0240e4f03147dcfe
]
