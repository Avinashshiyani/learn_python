from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length = 155 , label = 'username')
    password = forms.CharField(max_length = 155 , label = 'password' , widget = forms.Passwordinput)
    
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name" , "age" , "department"]