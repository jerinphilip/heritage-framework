from django.shortcuts import render
from django.http import HttpResponse
from .forms import MapImageForm
from django.contrib.gis.geos import Point
# Create your views here.
# def post_list(request):
#     return render(request, 'world/home.html', {})m

def post_list(request):
    form = MapImageForm()
    return render(request, 'world/home.html', {'form': form})