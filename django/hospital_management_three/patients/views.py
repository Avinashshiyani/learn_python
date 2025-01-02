from django.shortcuts import render  , redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

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
                return redirect("patient_records")
    else:
        form = LoginForm()
    return render(request , "login.html" , {'form':form})
