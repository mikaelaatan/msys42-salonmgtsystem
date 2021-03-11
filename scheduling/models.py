from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    staffid = models.AutoField(db_column='StaffID', primary_key=True, null=False)
    username = models.CharField(db_column='Username', max_length=15)

class ServiceRendered(models.Model):
    servicerenderedid = models.AutoField(db_column='ServiceRenderedID', primary_key=True)
    rating = models.DecimalField(db_column='Rating', max_digits=2, decimal_places=2, blank=True, null=True)
    comment = models.TextField(db_column='Comment', blank=True, null=True)
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=10, decimal_places=2, blank=True, null=True)
    paymentmethod = models.CharField(max_length=64, db_column='PaymentMethod')
    serviceid = models.ForeignKey('services.Service', db_column='ServiceID', on_delete=models.CASCADE)
    staffid = models.ForeignKey('Staff', db_column='StaffID', on_delete=models.CASCADE)

class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)
    username = models.CharField(db_column='Username', max_length=15)
    dateofbirth = models.DateField(null=False)

class Appointment(models.Model):
    appointmentid = models.AutoField(db_column='AppointmentID', primary_key=True)
    appointmentdate = models.DateField(null=False)
    appointmenttime = models.TimeField(null=False)
    iscancelled = models.BooleanField(default='No', null=False)
    customerid = models.ForeignKey('Customer', on_delete=models.CASCADE)

class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key = True)
    firstname = models.CharField(db_column='FirstName', max_length=24)
    lastname = models.CharField(db_column='LastName', max_length=12)
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50)
    contactnumber = models.IntegerField(db_column='ContactNumber')
    username = models.CharField(db_column='Username', max_length=15)
    password = models.CharField(db_column='Password', max_length=20)
