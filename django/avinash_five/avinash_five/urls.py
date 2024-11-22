from django.contrib import admin
from django.urls import path
from student.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_list),
    path('add/', student_add),
    path('delete/<id>/', student_delete),
    path('edit/<id>/', student_edit),
]
