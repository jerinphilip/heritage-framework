from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.gis.geos import *
# Create your models here.

class MapImage(models.Model):
	image = models.FileField(upload_to='uploads/')

class MapLocation(models.Model):
    #remove
	location1 = models.PointField("location1")
	# location2 = models.PointField("location2")                                                


class HeritageSite(models.Model):
    title = models.CharField("title", max_length=50)
    image = models.FileField(upload_to='uploads/')
    location_upper_left = models.PointField("location")
    location_lower_right = models.PointField("location")

class InterestPoint(models.Model):
    title = models.CharField("title", max_length=50)
    description = models.CharField("description", max_length=500 )
    location = models.PointField("location")
    def __str__(self):
        return self.title

class Image(models.Model):
    interest_point = models.ForeignKey('InterestPoint', on_delete=models.CASCADE)
    image = models.FileField(upload_to='./')
    caption = models.CharField('caption', max_length=200)

