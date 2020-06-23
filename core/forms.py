from django import forms
from .models import Appointment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Row, Layout

class CreateAppointmentForm(forms.ModelForm):
    venue = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Venue"}))
    class Meta:
        model = Appointment
        fields = ['plan','venue','date']
    
    

        