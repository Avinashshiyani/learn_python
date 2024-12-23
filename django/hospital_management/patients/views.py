from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import LoginForm, PatientForm

# Login View
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                return redirect('patient_records')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Show Patient Records
@login_required
def patient_records(request):
    patients = Patient.objects.all()
    return render(request, 'patient_records.html', {'patients': patients, 'user': request.user})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')
