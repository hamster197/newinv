"""zhem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.http import request
#from django.views.generic import DetailView,ListView

from . import views


app_name='avito_ap'
urlpatterns = [
    url(r'^avito/index$', views.AvitoIndexView, name='Avito_index'),
    url(r'^avito/detail/(?P<idd>[0-9]+)/$', views.AvitoDetailView, name='Avito_detail'),
    url(r'^avito/new$', views.newAvitoSub, name='Avito_new'),
    url(r'^avito/Gal/(?P<idd>[0-9]+)/$', views.AvitoGalView, name='Avito_new_galery'),
    url(r'^avito/Gal/del/(?P<idd>[0-9]+)/(?P<sidd>[0-9]+)/$', views.AvitiGalView, name='Avito_del_galery'),
    url(r'^avito/avito.xml$', views.avitoFeedView, name='Avito_feed'),
]
