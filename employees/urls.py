from django.urls import path
from . import views
from .views import *

app_name = 'employees'
urlpatterns = [
    path('',views.employees_list, name='employees-list'),    
]