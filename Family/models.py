from django.db import models

# Create your models here.

class Familia(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    has_children=models.BooleanField(null=True)
