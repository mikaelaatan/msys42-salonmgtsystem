from django.urls import path
from . import views
from .views import *

app_name = 'staff'
urlpatterns = [
    # path('add/', ServiceCreateView.as_view(), name='service-add'),
    path('signup/', signup_staff_view, name='signup-staff'),
    path('', StaffListView.as_view(), name='staff-list'),
    path('<int:id>/', views.dynamic_lookup_view, name='staff-detail'),
    path('edit/<int:id>/', StaffUpdateView.as_view(), name='staff-edit'),
    # path('delete/<int:id>/', StaffDeleteView.as_view(), name='staff-delete'),
]
