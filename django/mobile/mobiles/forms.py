from django import forms
from .models import Mobile

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['company', 'model', 'price', 'ram', 'storage']