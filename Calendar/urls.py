from django.conf.urls import url 
from . import views

app_name = "Calendar"
urlpatterns = [
    url('index/', views.index, name = 'index'),
    url('Calendar/', views.CalendarView.as_view(), name = 'calendar'),
    url('event/new/', views.create_event, name='event-new'),
    url('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event-edit'),
    url('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    url('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove-event"),
]