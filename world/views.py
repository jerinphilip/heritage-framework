from django.shortcuts import render
from django.http import HttpResponse
from .forms import MapImageForm
from django.contrib.gis.geos import Point
from django.contrib.gis.geos import GEOSGeometry

import datetime
import json
# import heritage.models as HeritageSite 
from .models import InterestPoint

from .forms import InterestPointForm
from .forms import UploadFileForm

# Create your views here.
# def post_list(request):
#     return render(request, 'world/home.html', {})m

def post_list(request):
	form = MapImageForm()
	return render(request, 'world/home.html', {'form': form})

# import heritage.forms as forms
# from django.contrib.gis.geos import Point
# from django.core.exceptions import ObjectDoesNotExist
# import heritage.models as HeritageSite 
# from heritage.models import InterestPoint 

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

# def image(request):
#     if request.method == 'POST':
#         form = forms.ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             imageObject = form.save()
#             image_file = form.cleaned_data.get('image')
#             add_image_location(image_file, imageObject)
#             html = "<html><body>Success!</body></html>"
#             return HttpResponse(html)
#         else:
#             html = "<html><body>"+str(form.errors)+"</body></html>"
#             return HttpResponse(html, status=400)
#     else:
#         form = forms.ImageForm()
#         return render(request, 'image.html', {'form': form})


# def interestpoint(request):
#     lul= GEOSGeometry('POINT (%d %d)' %( 17.382200, 78.398806), srid=4326)                 
#     llr = GEOSGeometry('POINT (%d %d)' %(17.384596, 78.403249), srid=4326)                 
#     form = forms.InterestPointForm(initial={'location': loc})
#     return render(request, 'map.html', {'rows':range(12), 'columns':range(12),'form':form, 'lul':lul, 'llr':llr, 'img_url':img_url})

def latitude(point):                                                    
	return float(point.y)                                                      

def longitude(point):                                                   
	return float(point.x)  

def gpsCoords(i,j,ul, lr,l,b):                                          
	add_lon=(latitude(lr)-latitude(ul))/2.0                        
	add_lat=(longitude(lr)-longitude(ul))/2.0                       
	lat = latitude(ul) +  add_lat*i + add_lat/2.0                                   
	lon = longitude(ul) + add_lon*j + add_lon/2.0                                  
	loc = GEOSGeometry('POINT (%f %f)' %(lon, lat))          
	return (loc)                                                        

# def interestpointlocation(request):
#     if request.method == 'POST':                                        
#         form = forms.InterestPointLocationForm(request.POST)            
#         if form.is_valid():                                             
#             form.save()                                                 
#         else:                                                           
#             html = "<html><body>"+str(form.errors)+"</body></html>"         
#             return HttpResponse(html, status=400)                       
#     else:                                                               
#         form = forms.InterestPointLocationForm()     
#         return render(request, 'interestpointlocation.html', {'form': form})


def index(request):
	return render(request, 'world/index.html')

# def heritage(request):
#     if request.method == 'POST':
#         form = forms.HeritageSiteForm(request.POST)
#         if form.is_valid():
#             form.save();
#         else:
#             html = "<html><body>"+str(form.errors)+"</body></html>"
#             return HttpResponse(html, status=400)


def mappage(request):
	return render(request, 'world/mappage.html')

def mapInteractive(request):
	if request.method == 'GET':
		img_url = '/static/golconda.jpg'
		ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
		lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
		location = gpsCoords(0,0, ul, lr,12,12)
		ip = InterestPoint.objects.filter(location=location)
		form = InterestPointForm(instance=ip[0])
		return render(request, 'world/map.html', {'rows':range(12), 'columns':range(12),'form':form, 'img_url':img_url})

def interestPointCreate(request):
	if request.method == 'POST':
		x = request.POST.get('x', None)
		y = request.POST.get('y', None)
		ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
		lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
		x = float(x)
		y = float(y)
		location = gpsCoords(x,y,ul, lr,12,12)
		
		#create
		form = InterestPointForm(request.POST)
		if form.is_valid():
			interest_point = InterestPoint(location=location)
			form = InterestPointForm(request.POST, instance=interest_point)
			form.save()
			img_url = '/static/golconda.jpg'
			form = InterestPointForm()
			return render(request, 'world/map.html', {'rows':range(12), 'columns':range(12),'form':form, 'img_url':img_url})   
		else:
			html = "<html><body>" +str(form.errors)+"</body></html>"
			return HttpResponse(html, status=400)
	

def interestPointEdit(request):

	if request.method == 'POST':
			x = request.POST.get('x', None)
			y = request.POST.get('y', None)
			ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
			lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
			x = float(x)
			y = float(y)
			location = gpsCoords(x,y,ul, lr,12,12)
			
			if form.is_valid():
				interest_point = InterestPoint.get(location=location)
				form = InterestPointForm(request.POST, instance=interest_point)
				form.save()
				img_url = '/static/golconda.jpg'
				form = InterestPointForm()
				return render(request, 'world/map.html', {'rows':range(12), 'columns':range(12),'form':form, 'img_url':img_url})
		
			else:
				html = "<html><body>" +str(form.errors)+"</body></html>"
				return HttpResponse(html, status=400)



def mapOperation(request):
	if request.method == 'GET':
		x = request.GET.get('x', None)
		y = request.GET.get('y', None)
		ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
		lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
		x = float(x)
		y = float(y)
		location = gpsCoords(x,y,ul, lr,12,12)
		interest_point = InterestPoint.objects.all().filter(location=location)
		if(len(interest_point)==0):
			return HttpResponse(json.dumps(response_data), content_type="application/json")

		if(len(interest_point)==1):
			return HttpResponse(json.dumps(response_data), content_type="application/json")

def mapForm(request):
	if request.method == 'GET':
		x = request.GET.get('x', None)
		y = request.GET.get('y', None)
		ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
		lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
		x = float(x)
		y = float(y)
		location = gpsCoords(x,y,ul, lr,12,12)
		interest_point = InterestPoint.objects.all().filter(location=location)
		if(len(interest_point)==0):
			form = InterestPointForm()
			return render(request, 'form.html', {'form':form, 'x':x, 'y':y})

		if(len(interest_point)==1):
			ip = InterestPoint.objects.filter(location=location)
			form = InterestPointForm(instance=ip[0])
			return render(request, 'form.html', {'form':form, 'x':x,'y':y})

	if request.method == 'POST':
			x = request.POST.get('x', None)
			y = request.POST.get('y', None)
			ul= GEOSGeometry('POINT (%f %f)' %( 17.382200, 78.398806))                 
			lr = GEOSGeometry('POINT (%f %f)' %(17.384596, 78.403249))                 
			x = float(x)
			y = float(y)
			location = gpsCoords(x,y,ul, lr,12,12)
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
					return render(request, 'world/map.html', {'rows':range(12), 'columns':range(12),'form':form, 'img_url':img_url})
		
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
				return render(request, 'world/map.html', {'rows':range(12), 'columns':range(12),'form':form, 'img_url':img_url})
				


def uploadFile(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST, request.FILES)
        	if form.is_valid():
            		imageObject = form.save()
            		html = "<html><body>"+"Success!"+"</body></html>"
            		return HttpResponse(html)
        	else:
            		html = "<html><body>"+str(form.errors)+"</body></html>"
            		return HttpResponse(html, status=400)
	if request.method == "GET":
		form = UploadFileForm();
		return render(request, 'uploadFile.html', {'form':form})
