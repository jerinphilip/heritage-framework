from django.http import HttpResponse
from django.shortcuts import render
import heritage.forms as forms
from django.contrib.gis.geos import Point
from heritage.utils import get_lat_long
from heritage.models import ImageLocation
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def add_image_location(image, img_obj):
    image.open('rb')
    (lat, lon) = get_lat_long(image)
    if lat is not None and lon is not None:
        location = Point(lat, lon)
        entry = ImageLocation(image=img_obj, location=location)
        entry.save()


def image(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            imageObject = form.save()
            image_file = form.cleaned_data.get('image')
            add_image_location(image_file, imageObject)
            html = "<html><body>Success!</body></html>"
            return HttpResponse(html)
        else:
            html = "<html><body>"+str(form.errors)+"</body></html>"
            return HttpResponse(html, status=400)
    else:
        form = forms.ImageForm()
        return render(request, 'image.html', {'form': form})


def interestpoint(request):
    if request.method == 'POST':
        form = forms.InterestPointForm(request.POST)
        if form.is_valid():
            form.save()
            html = "<html><body>Success!</body></html>"
            return HttpResponse(html)
        else:
            html = "<html><body>"+str(form.errors)+"</body></html>"
            return HttpResponse(html, status=400)
    else:
        form = forms.InterestPointForm()
        return render(request, 'interestpoint.html', {'form': form})


def interestpointlocation(request):
    if request.method == 'POST':
        pass
    else:
        form = forms.InterestPointLocationForm()
        return render(request, 'interestpointlocation.html', {'form': form})
