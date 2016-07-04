from django.contrib.gis import forms
import heritage.models as models


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = '__all__'


class InterestPointForm(forms.ModelForm):
    class Meta:
        model = models.InterestPoint
        fields = '__all__'


class InterestPointLocationForm(forms.ModelForm):
    class Meta:
        model = models.InterestPointLocation
        fields = '__all__'
