from django.shortcuts import render , redirect
from .models import *
# Create your views here.
def student_add(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("studentname")
        rollno = data.get("studentrollno")
        course = data.get("studentcourse")
        Student.objects.create(
        name = name,
        rollno = rollno,
        course = course,
        )
    
        return redirect("/add/")
    return render(request , "student_add.html")

def student_get(request):
    data = Student.objects.all()
    context = {
        "data":data
    }
    return render(request , "student_get.html" , context)