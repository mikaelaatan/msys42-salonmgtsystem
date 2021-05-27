from django.db import models
from django.urls import reverse
from datetime import timedelta

SERVICE_TYPE_CHOICES = [
    ('Hair', 'Hair Service'),
    ('Nails', 'Nail Service'),
    ('Skin', 'Skin Service'),
    ('Makeup', 'Semi-permanent Makeup'),
    ('Face', 'Facial Service'),
    ('Eyes', 'Eyebrow/Eyelash Service'),
]

# Create your models here.
class Service(models.Model):
    servicename = models.CharField("Service Name", max_length=64, unique=True)
    servicetype = models.CharField("Service Type", max_length=32,choices=SERVICE_TYPE_CHOICES, default="Hair Service")
    serviceprice = models.PositiveIntegerField("Price")
    servicedescription = models.TextField("Description", blank=True, null=True)
    serviceduration = models.DurationField("Duration",default=timedelta(minutes=20))

    def __str__(self):
        return str(self.servicetype).upper() + ": " + str(self.servicename)

    def get_absolute_url(self):
        return reverse("services:service-detail", kwargs={"id": self.id})

        # return f"/services/{self.id}"

    def serviceduration_HHmm(self):
        sec = self.serviceduration.total_seconds()
        return '%02d:%02d' % (int((sec/3600)%3600), int((sec/60)%60))

    def getservicename(self):
        return servicename

    def getserviceprice(self):
        return serviceprice
