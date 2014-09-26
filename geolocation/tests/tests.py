# coding=utf-8
from django.test import TestCase
from django.db.models.aggregates import Max
from ..models import GeoPolygon, Country, AdmDivision
from ..load import run


class TestGeolocation(TestCase):

    def setUp(self):
        pass

    def test_load_data(self):
        run()
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(AdmDivision.objects.filter(level=1).count(), 15)
        self.assertEqual(AdmDivision.objects.count(), 15)
        self.assertEqual(AdmDivision.objects.aggregate(max_level=Max('level'))['max_level'], 1)