from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import RedirectView

from collector.views import *

urlpatterns = patterns('',
	url(r'^$', InscritView.as_view(), name='inscription'),
#	url(r'^/reussite/$', views.inscription_reussie, name='inscription_reussie'),
	)
