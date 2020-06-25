from django import forms
from .models import Appointment, UserProfile
from crispy_forms.helper import FormHelper

from django.utils import timezone
from crispy_forms.layout import Column, Row, Layout
import datetime

class CreateAppointmentForm(forms.ModelForm):
    venue = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Venue"}))
    phone = forms.CharField(max_length=10 ,widget=forms.TextInput(attrs={'placeholder':"Phone Number"}))
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1',
            'placeholder': 'Select Date and Time',
        })
    )
    
    class Meta:
        model = Appointment
        fields = ['plan','venue','phone','date']
    def clean_phone(self,*args, **kwargs):
        phone = self.cleaned_data['phone']
        for i in phone:
            if not (i in '0123456789'):
                raise forms.ValidationError('Please Enter a phone number')
        return phone
    
    def clean_date(self,*args, **kwargs):
        date = self.cleaned_data['date']
        if date <= timezone.now():
            raise forms.ValidationError('Please Choose a date and time in the future')
        return date


class AppointmentImageUpload(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'picture')