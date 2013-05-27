from django.conf.urls import patterns, url
import sys, os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# Put your path to folder where finished encode downloads
# will be served from

MEDIA_DOWNLOADS_ROOT = os.path.join(os.getcwd(),'media/finished/')

urlpatterns = patterns('',
    # The main page:
    url(r'^$', 'traversme.encoder.views.home', name='home'),
    # Serves files from root/downloads/
    (r'^downloads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_DOWNLOADS_ROOT}),
)
