from django.conf.urls import url
from . import views
from django.contrib.gis import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from mysite import settings

# from  import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.mappage, name=''),
    url(r'^mapInteractive/$', views.mapInteractive, name='mapInteractive'),
    # url(r'^mapInteractive/create/$', views.interestPointCreate),
    # url(r'^mapInteractive/edit/$', views.interestPointEdit),
    # url(r'^mapOperation/$', views.mapOperation, name='mapOperation'),
    # url(r'^mapOperation/$', views.mapOperation, name='mapOperation'),

    url(r'^uploadFile/$', views.uploadFile),
    url(r'^form/$', views.mapForm),
    url(r'^testsample/$', views.testsample),
    url(r'^contact/$', views.contact),
    url(r'^about/$', views.about),
    url(r'^heritage/$', views.heritage),
    url(r'^addheritage/$', views.addHeritage),
    url(r'^delete/([0-9]+)/$', views.delete),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static('uploads/', document_root=settings.MEDIA_ROOT)