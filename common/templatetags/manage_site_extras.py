from django import template
from math import floor
from datetime import date, time, timedelta
# from appointment.models import AppointmentTime

register = template.Library()

def format_time(val):
	if val is not None:
		return val.strftime("%Y-%m-%dT%H:%M:%S")

def add_time(val):
	if val is not None:
		length = AppointmentTime.objects.last().length
		added_val = val + timedelta(hours=length)
		return added_val


register.filter('format_time', format_time)
