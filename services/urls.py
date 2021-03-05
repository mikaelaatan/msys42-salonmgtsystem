from django.urls import path
from . import views

urlpatterns = [
    path('serviceslist/', views.listofservices_view),
    path('addservice/', views.addservice_view),
]
