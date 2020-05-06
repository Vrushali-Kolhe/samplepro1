from django.db import models

# Create your models here.
from django.db.models import IntegerField


class employee(models.Model):
    name =models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    salary = models.IntegerField()