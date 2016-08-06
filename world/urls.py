from django.conf.urls import url
from . import views
from django.contrib.gis import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
# from  import settings
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]