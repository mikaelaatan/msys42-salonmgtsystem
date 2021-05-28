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
    required_css_class = 'required'


    servicename = forms.CharField(label='Name',error_messages = {
                 'unique':"This service already exists. Please try again."}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    servicetype = forms.ChoiceField(label='Service Type',choices=SERVICE_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    serviceprice = forms.DecimalField(label="Price",decimal_places=2, help_text="Php", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    serviceduration = forms.CharField(label='Duration',initial="00:00", help_text="Please use the following format: HH:MM.", widget=forms.TimeInput(attrs={'class': 'form-control'}))
    servicedescription = forms.CharField(required=False,label='Description',widget=forms.Textarea(attrs={'rows':3, 'class': 'form-control'}))


    class Meta:
        model = Service
        fields = '__all__'

    def clean_servicename(self):
        return self.cleaned_data['servicename'].capitalize()

    def clean_serviceduration(self):
        dur = self.cleaned_data['serviceduration']
        durstr = str(dur)
        print(durstr)
        print(len(durstr))
        if len(durstr) >= 6:
            dur_str = durstr[:-3]
            print(dur_str)
            t = datetime.strptime(dur_str,'%H:%M')
            delta = timedelta(hours=t.hour, minutes=t.minute)
            return delta
        dur_str = durstr+":00"
        print(dur_str)
        dur_str = dur_str[:-3]
        t = datetime.strptime(dur_str,'%H:%M')
        delta = timedelta(hours=t.hour, minutes=t.minute)
        return delta
