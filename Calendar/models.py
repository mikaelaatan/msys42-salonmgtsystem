from django.db import models

from django.urls import reverse
from services.models import Service
from staff.models import StaffModel
from customers.models import Customer

# Create your models here.
#servicename = models.CharField(Service, on_delete=models.CASCADE)
#clientname = models.TextField(Customer, on_delete=models.CASCADE)
#staffname = models.TextField(StaffModel, on_delete=models.CASCADE)

class Event(models.Model):
    servicename = models.CharField(max_length=20, default='')
    clientname = models.CharField(max_length=50, default = '')
    staffname = models.CharField(max_length=50, default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.servicename
    
    def get_absolute_url(self):
        return reverse('Calendar:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('Calendar:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
