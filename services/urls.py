from django.urls import path
from . import views
from .views import *

app_name = 'services'
urlpatterns = [
    # path('', views.serviceslist_view),
    path('', servicelist_view, name='service-list'),
    path('<int:id>/', views.dynamic_lookup_view, name='service-detail'),
    path('add/', ServiceCreateView.as_view(), name='service-add'),
    path('edit/<int:id>/', ServiceUpdateView.as_view(), name='service-edit'),
    path('delete/<int:id>/', ServiceDeleteView.as_view(), name='services-delete'),
]
