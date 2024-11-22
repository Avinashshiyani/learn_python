from django.shortcuts import render , redirect
from .models import *
# Create your views here.
def student_add(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("studentname")
        roll = data.get("studentroll")
        Student.objects.create(
            name = name,
            roll = roll,
        )
        return redirect("/add/")
    return render(request , "student_add.html")


def student_list(request):
    data = Student.objects.all()
    context = {
        "data":data
    }
    return render(request , "student_list.html", context)

def student_delete(request , id):
    data = Student.objects.get(id = id)
    data.delete()
    return redirect("/")

def student_edit(request , id):
    data = Student.objects.get(id = id)
    
    if request.method == "POST":
        value = request.POST
        data.name = value.get("studentname")
        data.roll = value.get("studentroll")
        data.save()
        return redirect("/")
    context = {
        "data":data 
    }
        
    return render(request , "student_edit.html" , context)
    