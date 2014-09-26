# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GeoPolygon'
        db.create_table(u'geolocation_geopolygon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_gadm', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('name_var', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('name_non_latin', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('valid_from', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('valid_to', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
            ('shape_leng', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('shape_area', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site'])),
        ))
        db.send_create_signal('geolocation', ['GeoPolygon'])

        # Adding model 'Country'
        db.create_table(u'geolocation_country', (
            (u'geopolygon_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['geolocation.GeoPolygon'], unique=True, primary_key=True)),
            ('iso', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('iso2', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('name_iso', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('name_local', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('geolocation', ['Country'])

        # Adding model 'AdmDivision'
        db.create_table(u'geolocation_admdivision', (
            (u'geopolygon_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['geolocation.GeoPolygon'], unique=True, primary_key=True)),
            ('country_iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adm_divisions', null=True, on_delete=models.SET_NULL, to=orm['geolocation.Country'])),
            ('level', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('parent_id_gadm', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, on_delete=models.SET_NULL, to=orm['geolocation.AdmDivision'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('geolocation', ['AdmDivision'])

        # Adding model 'GeographicArea'
        db.create_table(u'geolocation_geographicarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site'])),
        ))
        db.send_create_signal('geolocation', ['GeographicArea'])

        # Adding M2M table for field contains on 'GeographicArea'
        m2m_table_name = db.shorten_name(u'geolocation_geographicarea_contains')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('geographicarea', models.ForeignKey(orm['geolocation.geographicarea'], null=False)),
            ('geopolygon', models.ForeignKey(orm['geolocation.geopolygon'], null=False))
        ))
        db.create_unique(m2m_table_name, ['geographicarea_id', 'geopolygon_id'])

        # Adding model 'GeoPoint'
        db.create_table(u'geolocation_geopoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('coords', self.gf('django.contrib.gis.db.models.fields.PointField')(geography=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site'])),
        ))
        db.send_create_signal('geolocation', ['GeoPoint'])

        # Adding model 'Place'
        db.create_table(u'geolocation_place', (
            (u'geopoint_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['geolocation.GeoPoint'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal('geolocation', ['Place'])


    def backwards(self, orm):
        # Deleting model 'GeoPolygon'
        db.delete_table(u'geolocation_geopolygon')

        # Deleting model 'Country'
        db.delete_table(u'geolocation_country')

        # Deleting model 'AdmDivision'
        db.delete_table(u'geolocation_admdivision')

        # Deleting model 'GeographicArea'
        db.delete_table(u'geolocation_geographicarea')

        # Removing M2M table for field contains on 'GeographicArea'
        db.delete_table(db.shorten_name(u'geolocation_geographicarea_contains'))

        # Deleting model 'GeoPoint'
        db.delete_table(u'geolocation_geopoint')

        # Deleting model 'Place'
        db.delete_table(u'geolocation_place')


    models = {
        'geolocation.admdivision': {
            'Meta': {'object_name': 'AdmDivision', '_ormbases': ['geolocation.GeoPolygon']},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adm_divisions'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['geolocation.Country']"}),
            'country_iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'geopolygon_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['geolocation.GeoPolygon']", 'unique': 'True', 'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['geolocation.AdmDivision']"}),
            'parent_id_gadm': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'geolocation.country': {
            'Meta': {'object_name': 'Country', '_ormbases': ['geolocation.GeoPolygon']},
            u'geopolygon_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['geolocation.GeoPolygon']", 'unique': 'True', 'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'iso2': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'name_iso': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'name_local': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'})
        },
        'geolocation.geographicarea': {
            'Meta': {'object_name': 'GeographicArea'},
            'contains': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['geolocation.GeoPolygon']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"})
        },
        'geolocation.geopoint': {
            'Meta': {'object_name': 'GeoPoint'},
            'coords': ('django.contrib.gis.db.models.fields.PointField', [], {'geography': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"})
        },
        'geolocation.geopolygon': {
            'Meta': {'object_name': 'GeoPolygon'},
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_gadm': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'name_non_latin': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name_var': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'valid_from': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'valid_to': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        'geolocation.place': {
            'Meta': {'object_name': 'Place', '_ormbases': ['geolocation.GeoPoint']},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'geopoint_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['geolocation.GeoPoint']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['geolocation']