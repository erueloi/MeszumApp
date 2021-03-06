from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from geopy.geocoders.googlev3 import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError
from urllib2 import URLError


class Space(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    logotype = models.ImageField(upload_to='logos', blank=True)
    user = models.ForeignKey(User, unique= True)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    startdate = models.DateTimeField()
    poster = models.ImageField(upload_to='events', blank=True)
    address = models.CharField(max_length=100, blank=True)
    geometry = gis_models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)
    space = models.ForeignKey(Space)
    objects = gis_models.GeoManager()

    def save(self, **kwargs):
        if not self.geometry:
            address = u'%s' % (self.address)
            address = address.encode('utf-8')
            geocoder = GoogleV3()
            try:
                _, latlon = geocoder.geocode(address)
            except (URLError, GeocoderQueryError, ValueError):
                pass
            else:
                point = "POINT(%s %s)" % (latlon[1], latlon[0])
                self.geometry = geos.fromstr(point)
        super(Event, self).save()