from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.gis.geos import GEOSGeometry  

register = template.Library()

@register.simple_tag
def mapCoords(i,j):
        i=int(i)
        j=int(j)
        return "{}, {}, {}, {}".format(i*50,j*50,(i+1)*50,(j+1)*50)

def latitude(point):
    return point.y

def longitude(point):
    return point.x

@register.simple_tag
def gpsCoords(i,j,ul, lr,l,b):
        i=int(i)
        j=int(j)
        
        add_long=(latitude(lr)-latitude(ul))/2.0
        add_lat=(longitude(lr)-longitude(ul))/2.0
        
        lat = add_lat*i + add_lat/2.0
        lon = add_long*j + add_lon/2.0
        loc = GEOSGeometry('POINT (%d %d)' %(lon, lat), srid=4326)

        return (loc)

