from django import forms
from .models import Batch

class BatchForm(forms.ModelForm):

    class Meta:
        model = Batch
        exclude = ('created_on' , 'updated_on',)