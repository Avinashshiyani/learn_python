from django import forms
from .models import Patient
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label = 'username' , max_length = 155)
    password = forms.CharField(label = 'password' , max_length = 155 , widget = forms.PasswordInput)
    
    
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name" , "age" , "department"]
    