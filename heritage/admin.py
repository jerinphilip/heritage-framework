from django.contrib.gis import admin
import heritage.models as models

admin.site.register(models.InterestPointLocation, admin.OSMGeoAdmin)
admin.site.register(models.ImageLocation, admin.OSMGeoAdmin)
admin.site.register(models.Image)
admin.site.register(models.InterestPoint)
