from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user')
    birthdate = models.DateField(null=True)
    phone_number = models.CharField(max_length = 11)

    def __str__(self, *args, **kwargs):
        return f'{self.user.first_name} {self.user.last_name}'
