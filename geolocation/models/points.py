# coding=utf-8
from django.conf import settings
from django.contrib.gis.db.models import Model, PointField, GeoManager
from django.contrib.gis.measure import D
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ..managers import CurrentSiteGeoManager


class PointManagerMixin(object):
    def near_to(self, pnt, max_km):
        return self.get_queryset().filter(
            coords__distance_lte=(pnt, D(km=max_km))
        ).distance(pnt)


class GeoPointManager(GeoManager, PointManagerMixin):
    pass


class GeoPointCurrentSiteManager(CurrentSiteGeoManager, PointManagerMixin):
    pass


class GeoPoint(Model):
    coords = PointField(verbose_name=_(u"geographic coordinates"), geography=True)
    latitude = models.CharField(_(u"latitude"), max_length=50)
    longitude = models.CharField(_(u"longitude"), max_length=50)
    site = models.ForeignKey(Site, default=settings.SITE_ID)

    objects = GeoPointManager()
    on_site = GeoPointCurrentSiteManager()

    class Meta:
        app_label = 'geolocation'

    def __unicode__(self):
        return "Lat: %s, Lon: %s" % (self.latitude, self.longitude)