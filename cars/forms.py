from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import widgets
from datetime import datetime

from .models import VehicleMaintenance


# for DateTime input use
class MyDateTimeInput(forms.DateTimeInput):
    input_type = 'date'

# for DateTime input use
class MyTimeInput(forms.TimeInput):
    input_type = 'date'


# for Date input use
class MyDateInput(forms.DateInput):
    input_type = 'date'


class VehicleMaintenanceForm(forms.ModelForm):
    class Meta:
        model = VehicleMaintenance
        exclude = ["user","date_created"]

        widgets = {
            'car': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'date_maintained': MyTimeInput(attrs={'class': 'form-control'}),  
            'amount_spent': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),                
        }




