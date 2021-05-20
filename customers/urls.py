from django.urls import path
from .views import signup_view, home

urlpatterns = [
    path('signup/', signup_view, name = 'signup'),
    path('', home, name="home"),
    path('home/', home, name="home"),
]
