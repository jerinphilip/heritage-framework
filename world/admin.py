from django.contrib import admin

# Register your models here.
from .models import MapImage
from .models import MapLocation

admin.site.register(MapImage)
admin.site.register(MapLocation)