from django.conf.urls import patterns, url

from geonode.urls import *

urlpatterns = patterns('',

    # Static pages
   	url(r'^$', 'geonode.views.index', {'template': 'site_index.html'}, name='home'),
	url(r'^polls/$', 'polls.views.index'),
	url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
	url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
	url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
 ) + urlpatterns
