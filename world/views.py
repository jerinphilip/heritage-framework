from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import MapImageForm
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import GEOSGeometry

import datetime
import json 

from .models import InterestPoint
from .models import Image
from .models import HeritageSite

from .forms import HeritageSiteForm
from .forms import InterestPointForm
from .forms import UploadFileForm

def post_list(request):
	form = MapImageForm()
	return render(request, 'world/home.html', {'form': form})

def latitude(point):                                                    
	return float(point.y)                                                      

def longitude(point):                                                   
	return float(point.x)  

def gpsCoords(i,j,ul, lr,l,b):                                          
	add_lon = (latitude(lr) - latitude(ul))/2.0                        
	add_lat = (longitude(lr) - longitude(ul))/2.0                       
	lat = latitude(ul) +  add_lat*i + add_lat/2.0                                   
	lon = longitude(ul) + add_lon*j + add_lon/2.0                                  
	loc = GEOSGeometry('POINT (%f %f)' %(lon, lat))          
	return (loc)                                                       

def index(request):
	return render(request, 'world/index.html')

def mappage(request):
	return render(request, 'world/mappage.html')

def mapInteractive(request):
	if request.method == 'GET':
		img_url = '/static/golconda.jpg'
		ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
		lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
		location = gpsCoords(0,0, ul, lr,19,19)
		ip = InterestPoint.objects.filter(location=location)
		#form = InterestPointForm(instance=ip[0])
		form = InterestPointForm()
		return render(request, 'world/map.html', {'rows':range(19), 'columns':range(19),'form':form, 'img_url':img_url})


def mapForm(request):
	if request.method == 'GET':
		x = request.GET.get('x')
		y = request.GET.get('y')
		ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
		lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
		x = float(x)
		y = float(y)
		location = gpsCoords(x,y,ul, lr,19,19)
		interest_point = InterestPoint.objects.all().filter(location=location)
		if(len(interest_point)==0):
			form = InterestPointForm()
			return render(request, 'form.html', {'form':form, 'x':x, 'y':y})

		if(len(interest_point)==1):
			ip = InterestPoint.objects.filter(location=location)
			form = InterestPointForm(instance=ip[0])
			images = Image.objects.filter(interest_point=ip[0])
			return render(request, 'form.html', {'form':form, 'x':x,'y':y, 'images':images})

	if request.method == 'POST':
			x = request.POST.get('x')
			y = request.POST.get('y')
			ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
			lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
			x = float(x)
			y = float(y)
			location = gpsCoords(x,y,ul, lr,19,19)
			interest_points = InterestPoint.objects.all().filter(location=location)
			if(len(interest_points)==0):
				# create and save
				form = InterestPointForm(request.POST)
				if form.is_valid():
					interest_point = InterestPoint(location=location)
					form = InterestPointForm(request.POST, instance=interest_point)
					form.save()
					img_url = '/static/golconda.jpg'
					form = InterestPointForm()
					return render(request, 'world/map.html', {'rows':range(19), 'columns':range(19),'form':form, 'img_url':img_url})
		
				else:
					html = "<html><body>" +str(form.errors)+"</body></html>"
					return HttpResponse(html, status=400)
			if(len(interest_points)==1):
				#edit save
				interest_point = interest_points[0] #will work only when location is primary key
				form = InterestPointForm(request.POST, instance=interest_point)
				form.save()
				img_url = '/static/golconda.jpg'
				form = InterestPointForm()
				return render(request, 'world/map.html', {'rows':range(19), 'columns':range(19),'form':form, 'img_url':img_url})
				

def uploadFile(request):
	if request.method == "POST":
		img_url = '/static/golconda.jpg'
		ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
		lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
		location = gpsCoords(0,0, ul, lr,19,19)
		ip = InterestPoint.objects.filter(location=location)
		form = InterestPointForm(instance=ip[0])
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			imageObject = form.save()
			return render(request, 'world/mappage.html', {'rows':range(19), 'columns':range(19),'form':form, 'img_url':img_url})
		
		else:
			html = "<html><body>"+str(form.errors)+"</body></html>"
			return HttpResponse(html, status=400)
	if request.method == "GET":
		form = UploadFileForm();
		return render(request, 'uploadFile.html', {'form':form})

def testsample(request):
	return render(request, 'world/test.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def addHeritage(request):
	form = HeritageSiteForm()
	if request.method == 'POST':
		form = HeritageSiteForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			# return render(request, 'addheritage.html')
			return HttpResponseRedirect('/heritage/')
		
		else:
			html = "<html><body>"+str(form.errors)+"</body></html>"
			return HttpResponse(html, status=400)

	return render(request, 'addheritage.html', {'form': form} )

def heritage(request):
	if request.method == 'GET':
		sites = HeritageSite.objects.all()
		return render(request, 'heritage.html', {'sites':sites})
	# return render(request, 'heritage.html')

def delete(request,id):
	u = Image.objects.get(pk=id).delete()
	img_url = '/static/golconda.jpg'
	return render(request, 'world/map.html', {'rows':range(19), 'columns':range(19), 'img_url':img_url})
