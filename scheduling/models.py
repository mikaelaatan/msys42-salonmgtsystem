from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from staff.models import StaffModel
from customers.models import Customer
from django.urls import reverse

class Appointment(models.Model):
    appdatetime = models.DateTimeField('Start Date Time', blank=True,null=False)
    enddatetime = models.DateTimeField('End Date Time', blank=True,null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffModel,  on_delete=models.CASCADE)
    # totalamount = models.DecimalField(db_column='TotalAmount', max_digits=10, decimal_places=2, blank=True, null=True)
    # paymentmethod = models.CharField(max_length=64, db_column='PaymentMethod')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    iscancelled = models.BooleanField('Is it Cancelled', default=False, null=False)

    def __str__(self, *args, **kwargs):
        return f'{self.customer.user.username} booked {self.service.servicename} for {self.appdatetime}'

    def get_absolute_url(self):
        return reverse("scheduling:booking-details", kwargs={"id": self.id})
