from django import forms
from .models import Service

SERVICE_TYPE_CHOICES = [
    ('Hair', 'Hair Service'),
    ('Nails', 'Nail Service'),
    ('Skin', 'Skin Service'),
    ('Makeup', 'Semi-permanent Makeup'),
    ('Face', 'Facial Service'),
    ('Eyes', 'Eyebrow/Eyelash Service'),
]

class ServiceForm(forms.ModelForm):

    servicename = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    servicetype = forms.ChoiceField(label='Service Type',choices=SERVICE_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    serviceprice = forms.DecimalField(label='Price',decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    serviceduration = forms.DurationField(label='Duration',initial="00:00:00", widget=forms.TimeInput(attrs={'class': 'form-control'}))
    servicedescription = forms.CharField(required=False,label='Description',widget=forms.Textarea(attrs={'rows':3, 'class': 'form-control'}))

    class Meta:
        model = Service
        fields = '__all__'
       

    

