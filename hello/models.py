from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class AreaLatLon(models.Model):
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
