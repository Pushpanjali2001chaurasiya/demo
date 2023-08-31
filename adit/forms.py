from django import forms
from .models import *

class studentFrom(forms.ModelForm):
    class Meta:
        model = students
        fields ='__all__'
        