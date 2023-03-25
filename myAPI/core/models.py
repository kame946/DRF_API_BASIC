from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)