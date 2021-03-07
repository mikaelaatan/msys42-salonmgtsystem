from django import forms

from .models import Service

SERVICE_TYPE_CHOICES = [
    ('hair', 'Hair Service'),
    ('nails', 'Nail Service'),
    ('skin', 'Skin Service'),
    ('makeup', 'Semi-permanent Makeup'),
    ('face', 'Facial Service'),
    ('eyes', 'Eyebrow/Eyelash Service'),
]

# class ServiceCreateForm(forms.ModelForm):
#     class Meta:
#         model = Service
#         fields = '__all__'

class ServiceForm(forms.Form):
    servicename = forms.CharField(label='Name')
    servicetype = forms.ChoiceField(label='Service Type',choices=SERVICE_TYPE_CHOICES)
    serviceprice = forms.DecimalField(label='Price',decimal_places=2)
    serviceduration = forms.DurationField(label='Duration')
    servicedescription = forms.CharField(label='Description',widget=forms.Textarea(attrs={'rows':3}))
