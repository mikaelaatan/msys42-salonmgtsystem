from django.contrib import admin

from .models import Service
from .models import Staff
from .models import ServiceRendered
from .models import Customer
from .models import Appointment
from .models import User


admin.site.register(Service)
admin.site.register(Staff)
admin.site.register(ServiceRendered)
admin.site.register(Customer)
admin.site.register(Appointment)
admin.site.register(User)