# coding=utf-8
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from ..managers import CurrentSiteGeoManager


class GeoPolygon(models.Model):
    id_gadm = models.IntegerField()

    name = models.CharField(max_length=75)  # TODO create a name field and make it multi-language
    name_var = models.CharField(max_length=150, blank=True)
    name_non_latin = models.CharField(max_length=50, blank=True)

    valid_from = models.CharField(max_length=25, blank=True)
    valid_to = models.CharField(max_length=25, blank=True)

    geom = models.MultiPolygonField(srid=4326)
    shape_leng = models.FloatField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)

    site = models.ForeignKey(Site, default=settings.SITE_ID)

    objects = models.GeoManager()
    on_site = CurrentSiteGeoManager()

    class Meta:
        app_label = 'geolocation'

    def __unicode__(self):
        return self.name

    @property
    def div_level(self):
        try:
            return AdmDivision.objects.get(pk=self.pk).level
        except AdmDivision.DoesNotExist:
            return 0


class Country(GeoPolygon):
    iso = models.CharField(max_length=3, unique=True)
    iso2 = models.CharField(max_length=2, unique=True)
    name_iso = models.CharField(max_length=75)
    name_local = models.CharField(max_length=75, blank=True)

    class Meta:
        app_label = 'geolocation'


class AdmDivision(GeoPolygon):
    country_iso = models.CharField(max_length=3)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL, related_name='adm_divisions')
    level = models.PositiveSmallIntegerField()
    parent_id_gadm = models.IntegerField(null=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    type = models.CharField(max_length=50)
    type_en = models.CharField(max_length=50)

    class Meta:
        app_label = 'geolocation'

    def __unicode__(self):
        return "%s %s (%s)" % (self.type, self.name, self.country_iso.upper())

    @property
    def full_name(self):
        return self.__unicode__()


class GeographicArea(models.Model):
    name = models.CharField(max_length=75)
    contains = models.ManyToManyField(GeoPolygon)

    site = models.ForeignKey(Site, default=settings.SITE_ID)

    objects = models.Manager()
    on_site = CurrentSiteManager()


    class Meta:
        app_label = 'geolocation'


