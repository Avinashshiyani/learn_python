from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length = 100 , label = "Username")
    password = forms.CharField(max_length = 100 , label = "Password" , widget = forms.PasswordInput)
    

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name" , "age" , "department"]