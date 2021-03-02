from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    ServiceName = models.CharField(max_length=64)
    ServiceType = models.CharField(max_length=32)
    ServicePrice = models.DecimalField(decimal_places=2, max_digits=1000)
    ServiceDescription = models.TextField(blank=True, null=True)
    ServiceDuration = models.CharField(max_length=32)

class Staff(models.Model):
    staffid = models.AutoField(db_column='StaffID', primary_key=True, null=False)
    firstname = models.CharField(max_length=32, db_column='FirstName', null=False)
    lastname = models.CharField(max_length=32, db_column='LastName', null=False)

class ServiceRendered(models.Model):
    servicerenderedid = models.AutoField(db_column='ServiceRenderedID', primary_key=True)
    rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=2, blank=True, null=True)
    comment = models.TextField(db_column='Comment', blank=True, null=True)
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=10, decimal_places=2, blank=True, null=True)
    paymentmethod = models.CharField(max_length=64, db_column='PaymentMethod')
    serviceid = models.ForeignKey(Service, db_column='ServiceID', on_delete=models.CASCADE)
    staffid = models.ForeignKey('Staff', db_column='StaffID', on_delete=models.CASCADE)

class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)
    firstname = models.CharField(max_length=64, null=False)
    lastname = models.CharField(max_length=64, null=False)
    dateofbirth = models.DateField(null=False)
    emailaddress = models.CharField(max_length=64, null=False)
    phonenumber = models.IntegerField(null=False)

class Appointment(models.Model):
    appointmentid = models.AutoField(db_column='AppointmentID', primary_key=True)
    appointmentdate = models.DateField(null=False)
    appointmenttime = models.TimeField(null=False)
    iscancelled = models.BooleanField(default='No', null=False)
    customerid = models.ForeignKey('Customer', on_delete=models.CASCADE)
