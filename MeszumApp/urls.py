from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from meszum import views, serializers
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'events', serializers.EventViewSet)

urlpatterns = patterns('',
    url(r'^$', views.commingsoon, name='commingsoon'),
    url(r'^startpage/', views.startpage, name='startpage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meszum/', include('meszum.urls')),
    #All Auth URLS
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'^accounts/', include('registration.backends.simple.urls')),
)

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',(r'^media/(?P<path>.*)','serve',{'document_root': settings.MEDIA_ROOT}), )