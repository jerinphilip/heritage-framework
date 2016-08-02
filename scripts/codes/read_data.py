"""Module to fetch GPS info from images.
"""

import exifread

def get_latitude(filepath):
    """Returns the GPS Latitude of the image.
    """
    image_file = open(filepath, 'rb')
    tags = exifread.process_file(image_file)
    return tags['GPS GPSLatitude']

def get_longitude(filepath):
    """Returns the GPS Longitude of the image.
    """
    image_file = open(filepath, 'rb')
    tags = exifread.process_file(image_file)
    return tags['GPS GPSLongitude']
