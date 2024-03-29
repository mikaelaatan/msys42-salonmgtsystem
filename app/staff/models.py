from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from django.urls import reverse

class StaffModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff')
    about = models.TextField("About", max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=11)
    service = models.ManyToManyField(Service, blank=False)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self, *args, **kwargs):
            return f'{self.user.first_name} {self.user.last_name}'

    def get_absolute_url(self):
        return reverse("staff:staff-detail", kwargs={"id": self.id})

    def getStaffName(self):
        return f'{self.user.first_name} {self.user.last_name}'
