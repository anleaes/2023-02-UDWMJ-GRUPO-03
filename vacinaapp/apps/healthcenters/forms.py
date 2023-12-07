from django import forms
from .models import Healthcenter

class HealthcenterForm(forms.ModelForm):

    class Meta:
        model = Healthcenter
        exclude = ('created_on' , 'updated_on',)