
from django.contrib.postgres.fields import *
from django.db import models, transaction, IntegrityError
from itertools import islice


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class AreaCoordinate(models.Model):
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    name = models.CharField(max_length=200)


class Problem(models.Model):
    mp_id = models.IntegerField(primary_key=True)
    boulder = models.BooleanField(default=True)
    location = ArrayField(models.CharField(max_length=500), blank=True, verbose_name='Location Of Climb')
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    name = models.TextField(verbose_name='Problem/Route Name')
    area_id = models.IntegerField(null=False)
    mp_url = models.URLField(verbose_name='Mountain Project Url', default='None')
    grade = models.CharField(max_length=30, verbose_name='Grade', default='None')
    gmap_url = models.URLField(verbose_name='Google Maps Url', default='None')


class ProblemProcessor(object):

    @staticmethod
    def get_by_area_id(area_id_filter):
        return Problem.objects.all().filter(area_id=area_id_filter)

    @staticmethod
    def save_problem(problem):
        try:
            with transaction.atomic():
                problem.save()
        except IntegrityError:
            transaction.rollback()
            raise

    @staticmethod
    def save_problems(problems):
        batch_size = 100

        while True:
            batch = list(islice(problems, batch_size))
            if not batch:
                break
            try:
                with transaction.atomic():
                    Problem.objects.bulk_create(batch, batch_size)
            except IntegrityError:
                transaction.rollback()
                raise

    def create_problem(self, mp_id, boulder, location, lat, lon, name, area_id, mp_url, grade):
        return Problem(mp_id=mp_id, boulder=boulder,
                       location=location, lat=lat, lon=lon, name=name,
                       area_id=area_id, mp_url=mp_url, grade=grade,
                       gmap_url=self.build_googlemaps_url(lat, lon))

    @staticmethod
    def delete_problems_by_area_id(area_id_filter):
        Problem.objects.filter(area_id=area_id_filter).delete()

    @staticmethod
    def build_googlemaps_url(lat, lon):
        return 'http://maps.google.com/maps?q=' + str(lat) + ',' + str(lon)
