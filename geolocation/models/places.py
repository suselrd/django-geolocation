# coding=utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .points import GeoPoint


class Place(GeoPoint):
    name = models.CharField(max_length=100, verbose_name=_(u"place name"))
    description = models.CharField(max_length=200, verbose_name=_(u"place description"), blank=True)

    class Meta:
        app_label = 'geolocation'

    def __unicode__(self):
        return self.name