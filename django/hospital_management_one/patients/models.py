from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length = 155)
    age = models.IntegerField()
    department = models.CharField(max_length = 155)

    def __srt__(self):
        return self.name   
        