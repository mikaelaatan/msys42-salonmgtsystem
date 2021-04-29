from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from staff.models import StaffModel
from customers.models import Customer

class Appointment(models.Model):
    avg_rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=1, blank=True, null=True)
    comment = models.TextField('Comment', blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    staff = models.ForeignKey(StaffModel,  on_delete=models.CASCADE)
    # totalamount = models.DecimalField(db_column='TotalAmount', max_digits=10, decimal_places=2, blank=True, null=True)
    # paymentmethod = models.CharField(max_length=64, db_column='PaymentMethod')
    appdatetime = models.DateTimeField('Appointment Date Time', blank=True,null=True)
    iscancelled = models.BooleanField('Cancelled', default='No', null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.customers.user.username)
        # return self.customers.user.last_name + " booked " +  self.service.servicename + " by " + self.staff.user.first_name + " " self.staff.user.last_name + " at " + str(self.appointmentdate) + ", " + str(self.appointmenttime)
