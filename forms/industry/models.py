from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=50)
    section=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(max_length=254)
    school=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    