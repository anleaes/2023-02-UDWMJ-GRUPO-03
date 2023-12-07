from django import forms
from .models import Vaccine

class VaccineForm(forms.ModelForm):

    class Meta:
        model = Vaccine
        exclude = ('created_on' , 'updated_on',)