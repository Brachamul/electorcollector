from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.base import RedirectView

from collector.views import *
from . import views

urlpatterns = patterns('',
	url(r'^$', InscritView.as_view(), name='inscription'),
	url(r'reussite/$', views.inscription_reussie, name='inscription_reussie'),
	url(r'modifier/(?P<email>[A-Z0-9._%+-@\w]+)&(?P<code>[\d]+)$', ModifyView.as_view(), name='modifier'),
	)
