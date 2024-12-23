from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Patient

# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

# Patient Form
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'department']
