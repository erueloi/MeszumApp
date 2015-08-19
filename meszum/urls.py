from django.conf.urls import patterns, url
from meszum import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login, name='login'),
        url(r'^admin/space/$', views.administrationspace, name='administrationspace'),
        url(r'^admin/events/$', views.administrationevents, name='administrationevents'),
        url(r'^admin/events/add/$', views.addevents, name='addevents'),
    )
