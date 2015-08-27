from django.conf.urls import patterns, url
from meszum import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login, name='login'),
        url(r'^accounts/register/$', views.login, name='registration_register'),
        url(r'^admin/superdash/$', views.superuserdashboard, name='superuserdashboard'),
        url(r'^admin/superdash/spaces$', views.sd_spaces, name='sd_spaces'),
        url(r'^admin/space/$', views.administrationspace, name='administrationspace'),
        url(r'^admin/events/$', views.administrationevents, name='administrationevents'),
        url(r'^admin/events/add/$', views.addevents, name='addevents'),
    )
