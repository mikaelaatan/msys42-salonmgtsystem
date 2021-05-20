from django.conf.urls import url 
from . import views

app_name = "Calendar"
urlpatterns = [
    url('index/', views.index, name = 'index'),
    url('Calendar/', views.CalendarView.as_view(), name = 'calendar'),
    url('event/new/', views.event, name='event_new'),
    url('event/edit/(?P<event_id>\d+)/', views.event, name='event_edit'),
]