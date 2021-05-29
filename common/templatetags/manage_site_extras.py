from django import template
from math import floor
from datetime import date, time, timedelta
# from appointment.models import AppointmentTime

register = template.Library()

def format_time(val):
	if val is not None:
		return val.strftime("%Y-%m-%dT%H:%M:%S")

register.filter('format_time', format_time)
