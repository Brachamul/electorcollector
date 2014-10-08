from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', include('collector.urls'), name="collector"),
	url(r'^admin/', include(admin.site.urls)),
)
