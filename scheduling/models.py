from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from staff.models import StaffModel
from customers.models import Customer

class Appointment(models.Model):
    avg_rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=1, blank=True, null=True)
    comment = models.TextField(db_column='Comment', blank=True, null=True)
    services = models.ForeignKey(Service, db_column='ServiceID', on_delete=models.CASCADE)
    staffs = models.ForeignKey(StaffModel, db_column='StaffID', on_delete=models.CASCADE)
    # totalamount = models.DecimalField(db_column='TotalAmount', max_digits=10, decimal_places=2, blank=True, null=True)
    # paymentmethod = models.CharField(max_length=64, db_column='PaymentMethod')
    appointmentdate = models.DateField(db_column='Appointment Date', blank=True,null=True)
    appointmenttime = models.CharField(db_column='Appointment Time', max_length=10,blank=True,null=True) #thinking of TimeField
    iscancelled = models.BooleanField(db_column='Cancelled', default='No', null=False)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.appointmentdate) + ", " + str(self.appointmenttime)
        # return self.customers.user.last_name + " booked " +  self.service.servicename + " by " + self.staff.user.first_name + " " self.staff.user.last_name + " at " + str(self.appointmentdate) + ", " + str(self.appointmenttime)
