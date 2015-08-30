from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from meszum import views

urlpatterns = patterns('',
    url(r'^$', views.commingsoon, name='commingsoon'),
    url(r'^startpage/', views.startpage, name='startpage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meszum/', include('meszum.urls')),
    #All Auth URLS
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^accounts/', include('registration.backends.simple.urls')),
)

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',(r'^media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}), )