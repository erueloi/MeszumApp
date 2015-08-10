from django.conf.urls import patterns, url
from meszum import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
    )
