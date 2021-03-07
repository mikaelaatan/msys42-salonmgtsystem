from django.urls import path
from . import views

app_name = 'services'
urlpatterns = [
    path('', views.serviceslist_view),
    path('add/', views.addservice_view, name='service-list'),
    path('<int:id>/', views.dynamic_lookup_view, name='service-detail')
    # path('services/<int:id>', views.dynamic_lookup_view, name='services-detail')
    # path('services/<int:id>', views.dynamic_lookup_view, name='services-detail')

]
