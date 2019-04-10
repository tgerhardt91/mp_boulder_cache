from django.db import models
from django.contrib.postgres.fields import *


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class AreaCoordinate(models.Model):
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    name = models.CharField(max_length=200)


class Problem(models.Model):
    mp_id = models.IntegerField()
    boulder = models.BooleanField(default=True)
    area = ArrayField(models.CharField(max_length=200), blank=True)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    area_id = models.IntegerField(null=False)
