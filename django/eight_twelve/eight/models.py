from django.db import models

# Create your models here.
class Eight(models.Model):
    name = models.TextField(max_length = 155)
    roll = models.IntegerField()
    
    