from django.contrib.gis.db import models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from polymorphic.models import PolymorphicModel
from django_poly_dag.models import node_factory, edge_factory


class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class BaseGeoNode(PolymorphicModel, node_factory('BaseGeoEdge')):
    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name


class GeoPumpNode(BaseGeoNode):
    # GeoDjango-specific: a geometry Point field
    point = models.PointField()

    def __str__(self):
        return str(self.name)


class GeoCanalNode(BaseGeoNode):
    # GeoDjango-specific: a geometry Point field
    line = models.LineStringField()

    def __str__(self):
        return str(self.name)


class BaseGeoEdge(PolymorphicModel, edge_factory('BaseGeoNode', concrete=False)):
    name = models.CharField(max_length = 32)

    def __str__(self):
        return self.name

