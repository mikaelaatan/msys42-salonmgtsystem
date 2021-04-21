from django import forms
from .models import Service
from datetime import datetime, timedelta

SERVICE_TYPE_CHOICES = [
    ('Hair', 'Hair Service'),
    ('Nails', 'Nail Service'),
    ('Skin', 'Skin Service'),
    ('Makeup', 'Semi-permanent Makeup'),
    ('Face', 'Facial Service'),
    ('Eyes', 'Eyebrow/Eyelash Service'),
]

class ServiceForm(forms.ModelForm):
    servicename = forms.CharField(label='Name',error_messages = {
                 'unique':"This service already exists. Please try again."})
    servicetype = forms.ChoiceField(label='Service Type',choices=SERVICE_TYPE_CHOICES)
    serviceprice = forms.DecimalField(label="Price",decimal_places=2, help_text="Php")
    serviceduration = forms.DurationField(label='Duration',initial="00:00", help_text="Please use the following format: <em>HH:MM</em>.")
    servicedescription = forms.CharField(required=False,label='Description',widget=forms.Textarea(attrs={'rows':3}))

    class Meta:
        model = Service
        fields = '__all__'

    def clean_servicename(self):
        return self.cleaned_data['servicename'].capitalize()

    def clean_serviceduration(self):
        dur = self.cleaned_data['serviceduration']
        # if isinstance(dur, datetime) == True:
        durstr = str(dur)
        dur_str = durstr[2:]
        # dur_str = ''.join([dur_str,":00"])
        t = datetime.strptime(dur_str,'%H:%M')
        delta = timedelta(hours=t.hour, minutes=t.minute)
        return delta
        # else:
        #     return delta
