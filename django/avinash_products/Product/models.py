from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 155)
    description = models.TextField()
    price = models.IntegerField()
