from django.db import models
from django.contrib.auth.models import User
from services.models import Service
from staff.models import StaffModel
from customers.models import Customer
from django.urls import reverse

import datetime
from datetime import datetime as dt
from django.utils import timezone

class Appointment(models.Model):
    appdatetime = models.DateTimeField('Start Date Time', blank=True,null=False)
    enddatetime = models.DateTimeField('End Date Time', blank=True,null=False)
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

    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
        return overlap

######## HELP HERE, NEED APPOINTMENTS TO NOT OVERLAP #################
    # def clean(self):
    #     date = self.appdatetime
    #     staff = self.staff
    #     service = self.service
    #     now = timezone.now()
    #     if date and staff:
    #         if date < now:
    #             raise forms.ValidationError('Cannot pick a past date for future appointment')
    #     events = Appointment.objects.filter(staff=staff, iscancelled=False)
    #     if events.exists():
    #         for event in events:
    #             if self.check_overlap(event.appdatetime, event.enddatetime, self.appdatetime, self.enddatetime):
    #                 raise forms.ValidationError('This date is already booked for this staff member')


    
            # booked_dates = Appointment.objects.filter(staff=staff, iscancelled=False).values_list('appdatetime', flat=True)
            # endbooked_dates = Appointment.objects.filter(staff=staff, iscancelled=False).values_list('enddatetime', flat=True)
            # for booked_date in booked_dates:
            #     if date >= booked_date and date < booked_date.enddatetime:
            #         raise forms.ValidationError('This date is already booked for this staff member')
