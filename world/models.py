from __future__ import unicode_literals

from django.contrib.gis.db import models
from django.contrib.gis.geos import *
# Create your models here.

class MapImage(models.Model):
	image = models.FileField(upload_to='uploads/')

class MapLocation(models.Model):
	location1 = models.PointField("location1")
	# location2 = models.PointField("location2")                                                