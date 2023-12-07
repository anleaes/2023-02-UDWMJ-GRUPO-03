from django import forms
from .models import Brand

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        exclude = ('created_on' , 'updated_on',)