from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.TextField(max_length = 155)
    rollno = models.IntegerField()
    course = models.TextField(max_length = 155)