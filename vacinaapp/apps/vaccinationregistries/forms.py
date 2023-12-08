from django import forms
from .models import VaccinationRegistry

class VaccinationRegistryForm(forms.ModelForm):

    class Meta:
        model = VaccinationRegistry
        exclude = ('created_on' , 'updated_on',)