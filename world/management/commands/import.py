import os
import world

from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping

from world.models import MapImage, MapLocation

class Command(BaseCommand):
    help = 'Loads geologic unit data from app data directory'

    def handle(self, *args, **options):
        unit_shp = os.path.abspath(os.path.join(os.path.join(os.path.dirname(world.__file__), 'data/cogeol.kml')))

        lm = LayerMapping(MapImage, MapLocation, 
            transform=False, encoding='iso-8859-1') 
        lm.save(strict=True, verbose=True)
