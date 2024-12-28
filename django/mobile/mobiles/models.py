from django.db import models

# Create your models here.
class Mobile(models.Model):
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ram = models.IntegerField()
    storage = models.IntegerField()