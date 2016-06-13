from django.contrib.gis.db import models


class InterestPoint(models.Model):
    title = models.CharField("title", max_length=50)
    description = models.CharField("description", max_length=500)


class InterestPointLocation(models.Model):
    interest_point = models.ForeignKey('InterestPoint', on_delete=models.CASCADE)
    location = models.PointField("location")
