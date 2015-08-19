from django.db import models
from django.contrib.auth.models import User


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
    space = models.ForeignKey(Space)
