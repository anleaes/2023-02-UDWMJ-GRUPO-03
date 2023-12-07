from django import forms
from .models import Professional

class ProfessionalForm(forms.ModelForm):

    class Meta:
        model = Professional
        exclude = ('created_on' , 'updated_on',)