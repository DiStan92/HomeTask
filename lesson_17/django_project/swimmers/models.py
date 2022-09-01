from django.db import models

# Create your models here.

class Swimmer(models.Model):
    age = models.IntegerField()
    time = models.TimeField()
