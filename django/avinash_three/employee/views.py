from django.shortcuts import render , redirect
from .models import *
# Create your views here.
def employee_add(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("employeename")
        sirname = data.get("employeesirname")
        salary = data.get("employeesalary")
        
        Employee.objects.create(
            name = name,
            sirname = sirname,
            salary = salary
        )
        
        return redirect("/add/")
    return render(request , "employee_add.html")

def employee_list(request):
    data = Employee.objects.all()
    context = {
        "data":data
    }
    return render(request , "employee_list.html" , context)

def employee_delete(request , id):
    data = Employee.objects.get(id = id)
    data.delete()
    return redirect("/")

def employee_edit(request , id):
    data = Employee.objects.get(id = id)

    if request.method == "POST":
        value = request.POST
        data.name = value.get("employeename")
        data.sirname = value.get("employeesirname")
        data.salary = value.get("employeesalary")
        data.save()
        return redirect("/")
        

    context = {
        "data":data
    }
    
    return render(request , "empoyee_edit.html" , context)