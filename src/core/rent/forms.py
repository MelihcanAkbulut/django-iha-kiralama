#forms.py
from django import forms  
from . import models


class RentForm(forms.ModelForm):  
    class Meta:  
        model = models.Rent  
        fields = ['user', 'product', 'startDate','endDate']
        widgets = { 
            'user': forms.NumberInput(attrs={ 'class': 'form-control' }), 
            'product': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'startDate': forms.DateTimeInput(attrs={ 'class': 'form-control' }),
            'endDate': forms.DateTimeInput(attrs={ 'class': 'form-control' })
      }
        