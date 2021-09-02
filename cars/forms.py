from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import widgets

from .models import CarOwnerDriverRegister


# for DateTime input use
class MyDateTimeInput(forms.DateTimeInput):
    input_type = 'date'

# for DateTime input use
class MyTimeInput(forms.TimeInput):
    input_type = 'date'


# for Date input use
class MyDateInput(forms.DateInput):
    input_type = 'date'


class CarOwnersDriversForm(forms.ModelForm):
    class Meta:
        model = CarOwnerDriverRegister
        exclude = ["user","date_created", "last_updated","active","created_by"]

        widgets = {
            'date_of_birth': MyDateInput(attrs={'class': 'form-control'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            # 'phone_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_2': forms.NumberInput(attrs={'class': 'form-control'}),
            'nationality': forms.Select(attrs={'class': 'form-control'}),
            'state_of_origin': forms.Select(attrs={'class': 'form-control'}),
            'lga_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
            'permanent_address': forms.TextInput(attrs={'class': 'form-control'}),
            'state_of_residence': forms.Select(attrs={'class': 'form-control'}),
            'lga_of_residence': forms.TextInput(attrs={'class': 'form-control'}),
            'address_of_residence': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin_relationship': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),           
            
        }



