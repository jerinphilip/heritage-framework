from django.contrib.gis.db import models


class InterestPoint(models.Model):
    title = models.CharField("title", max_length=50)
    description = models.CharField("description", max_length=500)
    def __str__(self):
        return self.title


class InterestPointLocation(models.Model):
    interest_point = models.ForeignKey('InterestPoint', on_delete=models.CASCADE)
    location = models.PointField("location")


class Image(models.Model):
    image = models.FileField(upload_to='uploads/')
    caption = models.CharField('caption', max_length=200)


class ImageLocation(models.Model):
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    location = models.PointField("location")
