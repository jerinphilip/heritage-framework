# from django.contrib.gis import forms                                    
# from django import forms\
from django.forms import ModelForm
from django.contrib.gis import forms
from .models import MapImage
from .models import MapLocation
from .models import HeritageSite
from .models import InterestPoint
from .models import Image


class MapImageForm(forms.ModelForm):
    class Meta:
        model = MapImage
        fields = '__all__'

class MapLocationForm(forms.ModelForm):
    class Meta:
        model = MapLocation
        fields = '__all__'

class HeritageSiteForm(forms.ModelForm):
    class Meta:
        model = HeritageSite
        title = forms.CharField(label='title')
        image = forms.FileField()
        location_upper_left = forms.PointField()
        location_lower_right = forms.PointField()
        exclude = ['location']

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'


class InterestPointForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    # title = forms.CharField(widget=forms.title)
    class Meta:
        model = InterestPoint
        title = forms.CharField(max_length=50)
        # description = forms.CharField(widget=forms.Textarea)    
        exclude = ['location']
    