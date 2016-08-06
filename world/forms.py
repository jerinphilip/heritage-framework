# from django.contrib.gis import forms                                    
from django import forms
from .models import MapImage
from .models import MapLocation

class MapImageForm(forms.ModelForm):
    
    class Meta:
        model = MapImage
        fields = '__all__'



class MapLocationForm(forms.ModelForm):
    
    class Meta:
        model = MapLocation
        fields = '__all__'