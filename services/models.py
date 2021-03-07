from django.db import models
from django.urls import reverse

# Create your models here.
class Service(models.Model):
    servicename = models.CharField(max_length=64)
    servicetype = models.CharField(max_length=32)
    serviceprice = models.DecimalField(decimal_places=2, max_digits=1000)
    servicedescription = models.TextField(blank=True, null=True)
    serviceduration = models.CharField(max_length=32)

    # def __str__(self):
    #     return str(self.id) + ": " + self.servicename + ", " + str(self.serviceprice)

    def get_absolute_url(self):
        return reverse("services:service-detail", kwargs={"id": self.id})

        # return f"/services/{self.id}"
