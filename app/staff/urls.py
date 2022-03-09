from django.urls import path
from . import views
from .views import *

app_name = 'staff'
urlpatterns = [
    path('add/', add_staff_view, name='signup-staff'),
    path('signup/', signup_staff_view, name='signup-staff'),
    path('', stafflist_view, name='staff-list'),
    path('<int:id>/', views.dynamic_lookup_view, name='staff-detail'),
    # path('edit/<int:id>/', StaffUpdateView.as_view(), name='staff-edit'),
    path('edit/<int:id>/', edit_staff_view, name='staff-edit'),
]
