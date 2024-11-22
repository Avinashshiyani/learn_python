from django.contrib import admin
from django.urls import path
from student.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', student_get ),
    path('add/', student_add ),
]
