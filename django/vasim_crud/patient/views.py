from django.shortcuts import render , redirect
from  .models import *
from  .forms import *
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user:
                login(request , user)
                return redirect("records")
    else:
        form = LoginForm()
    return render(request , "login.html" , {'form':form})
    
@login_required

def patient_record(request):
    patients = Patient.objects.all()
    return render(request , "records.html" , {'datas':patients , 'user':request.user})

def delete(request , id):
    data = Patient.objects.get(id = id)
    data.delete()
    return redirect('records')

def logout_view(request):
    logout(request)
    return redirect('login')