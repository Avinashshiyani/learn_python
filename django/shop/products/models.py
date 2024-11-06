from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(200)
    stock = models.PositiveIntegerField()
    
def __str__(self):
    return self.name

