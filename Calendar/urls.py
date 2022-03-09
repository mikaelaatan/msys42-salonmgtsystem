from django.urls import include, path
from . import views

app_name = "Calendar"
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('Calendar/', views.CalendarView.as_view(), name = 'calendar'),
    path('event/new/', views.create_event, name='event-new'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event-edit'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove-event"),
]