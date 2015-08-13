from django.conf.urls import patterns, url
from meszum import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.login, name='login'),
        url(r'^administrationspace/$', views.administrationspace, name='administrationspace'),
    )
