from django import forms
from collections import OrderedDict as SortedDict

from .models import Ride

class MyDateTimeInput(forms.DateTimeInput):
    input_type = 'date'

class BookRideForm(forms.ModelForm):
	class Meta:
		model = Ride
		# fields = ('pickup_address','destination','distance','service_class')
		exclude = ['date_created','updated']

		widgets = {
		'pickup_address': forms.TextInput(attrs={'class': 'form-control'}),
		'destination': forms.TextInput(attrs={'class': 'form-control'}),
		'distance': forms.HiddenInput(attrs={'class': 'form-control'}),
		'service_class': forms.Select(attrs={'class': 'form-control'}),
		# 'comments': forms.Select(attrs={'class': 'form-control'}),
		'ride_date': MyDateTimeInput(attrs={'class': 'form-control'}),                            
        'ride_time': forms.TimeInput(attrs={'type': 'time','class': 'form-control'}),				
        }



