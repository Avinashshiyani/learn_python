from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.TextField(max_length =  155)
    sirname = models.TextField(max_length = 155)
    salary = models.IntegerField()