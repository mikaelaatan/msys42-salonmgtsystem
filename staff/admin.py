from django.contrib import admin
from .models import StaffModel
from easy_select2 import select2_modelform

# Register your models here.
admin.site.register(StaffModel)
