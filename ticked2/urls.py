from django.conf.urls import patterns, include, url
from TODOs.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', view_todos),
    # Examples:
    # url(r'^$', 'ticked2.views.home', name='home'),
    # url(r'^ticked2/', include('ticked2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
