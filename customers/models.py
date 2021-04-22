from django.db import models

# Create your models here.

class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)
    username = models.OnetoOneField(User on_delete = ,  models.CASCADE, related_name='user')
    birthdate = models.DateField(null=False)
    phone_number = models.CharField(max_length = 11)
    city = models.CharField(max_length = 45)
    country = models.CharField(max_length = 45)

    def __str__(self, *args, **kwargs):
        return f'{self.user.first_name} {self.user.last_name}'
