from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user:
                login(request , user)
                return redirect('patient_records')
    else:
        form = LoginForm()
    return render(request , "login.html" , {'form': form})


def patient_records(request):
    patients = Patient.objects.all()
    return render(request , "patient_records.html" , {'patients':patients , 'user':request.user})

def logout_view(request):
    logout(request)
    return redirect('login')
    
    
        
        
