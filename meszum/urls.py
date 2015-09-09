from django.conf.urls import patterns, url
from meszum import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^accounts/register/$', views.login, name='registration_register'),
        url(r'^admin/superdash/$', views.superuserdashboard, name='superuserdashboard'),
        url(r'^admin/superdash/spaces$', views.sd_spaces, name='sd_spaces'),
        url(r'^admin/superdash/spaces/events/$', views.sd_events, name='sd_events'),
        url(r'^admin/superdash/spaces(?P<idspace>[0-9]+)/events/$', views.sd_events, name='sd_events'),
        url(r'^admin/superdash/users', views.sd_users, name='sd_users'),
        url(r'^admin/space/(?P<idspace>[0-9]+)/$', views.administrationspace, name='administrationspace'),
        url(r'^admin/space/profile/$', views.profilespace, name='profilespace'),
        url(r'^admin/space/profile/spacemodal/$', views.SpaceFormView.as_view(), name='space-modal'),
        url(r'^admin/space/eventmodal/$', views.EventFormView.as_view(), name='event-modal'),
        url(r'^admin/space/(?P<idspace>[0-9]+)/events/(?P<idevent>[0-9]+)/$', views.addevents, name='administrationevent'),
        url(r'^profile/', views.profile, name='profile'),
    )
