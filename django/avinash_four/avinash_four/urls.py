from django.contrib import admin
from django.urls import path
from employee.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', employee_list),
    path('add/', employee_add),
    path('delete/<id>', employee_delete),
    path('edit/<id>', employee_edit),
]
