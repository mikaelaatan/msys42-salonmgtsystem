from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('signup/', signup_view, name = 'signup'),
    # path('profile/<int:id>/', views.dynamic_lookup_view, name='customer-profile'),
]
