from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user')
    birthday = models.DateField(null=True)
    phone_number = models.CharField(max_length = 11)

    def __str__(self, *args, **kwargs):
        return f'{self.user.username} - {self.user.first_name} {self.user.last_name} - {self.phone_number}'

    def getCustomerName(self):
        return f'{self.user.first_name} {self.user.last_name}'

    # def get_absolute_url(self):
    #     return reverse("customer-profile", kwargs={"id": self.id})
