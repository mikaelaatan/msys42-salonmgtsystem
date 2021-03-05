from django.db import models
from django.forms import ModelForm

# Create your models here.
class Service(models.Model):
    ServiceName = models.CharField(max_length=64)
    ServiceType = models.CharField(max_length=32)
    ServicePrice = models.DecimalField(decimal_places=2, max_digits=1000)
    ServiceDescription = models.TextField(blank=True, null=True)
    ServiceDuration = models.CharField(max_length=32)

    # def __str__:
    #     return str()
