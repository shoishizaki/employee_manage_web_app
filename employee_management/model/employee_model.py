from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    home = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    