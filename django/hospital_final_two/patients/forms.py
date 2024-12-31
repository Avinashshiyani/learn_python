from django import forms 
from .models import *
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label = "username" , max_length = 155)
    password = forms.CharField(label = "password" , widget = forms.PasswordInput)
    
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name" , "age" , "department"]