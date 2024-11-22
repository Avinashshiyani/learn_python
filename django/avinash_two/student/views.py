from django.shortcuts import render , redirect
from .models import *

# Create your views here.
def student_add(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("studentname")
        roll = data.get("studentroll")
        course = data.get("studentcourse")
        
        Student.objects.create(
            name =name,
            roll =roll,
            course =course,
        )
        
        return redirect("/add/")
    return render(request , "student_add.html")

def student_list(request):
    data = Student.objects.all()
    context = {
        "data":data 
    }
    return render(request , "student_list.html" , context)
    
    