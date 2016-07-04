import os
from PIL import Image
from PIL.ExifTags import TAGS


def todec(q):
    x, y = q
    return x/(y*1.0)


def convert(l):
    d, m, s = map(todec, list(l))
    return (d + m/60.0 + s/3600.0)


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def get_lat_long(img):
    exif = get_exif(img)["GPSInfo"]
    try:
        lat = exif[2]
        lon = exif[4]
        #print(lat, lon)
        res = (convert(lat), convert(lon))
        return res 
    except:
        return (None, None)
