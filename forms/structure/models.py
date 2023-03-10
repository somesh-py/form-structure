from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=50)
    password=models.CharField(max_length=50)