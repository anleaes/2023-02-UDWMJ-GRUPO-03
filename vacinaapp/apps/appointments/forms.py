from django import forms
from .models import Appointment, Patient, AppointmentVaccine, Vaccine

class AppointmentForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        exclude = ('patient', 'created_on' , 'updated_on')

class AppointmentVaccineForm(forms.ModelForm):
    
    class Meta:
        model = AppointmentVaccine
        exclude = ('appointment', 'created_on' , 'updated_on')