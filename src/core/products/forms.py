#forms.py
from django import forms  
from . import models


class ProductForm(forms.ModelForm):  
    class Meta:  
        model = models.Products  
        fields = ['brand', 'model', 'category','weight', 'height', 'altitude', 'endurance', 'wingspan','payload']
        widgets = { 
            'brand': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'model': forms.TextInput(attrs={ 'class': 'form-control' }),
            'category': forms.TextInput(attrs={ 'class': 'form-control' }),
            'weight': forms.NumberInput(attrs={ 'class': 'form-control' }), 
            'height': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'altitude': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'endurance': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'wingspan': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'payload': forms.NumberInput(attrs={ 'class': 'form-control' }),
      }
        