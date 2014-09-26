# coding=utf-8
from django.contrib.gis.admin import site, GeoModelAdmin
from .models.places import Place
from .models.areas import GeoPolygon


site.register(Place, GeoModelAdmin)
site.register(GeoPolygon, GeoModelAdmin)