from django.conf.urls import patterns, include, url
from Service.views import *
from content import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Service.views.home', name='home'),
    # url(r'^Service/', include('Service.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^content/(?P<content_slug>\w+)/$',content  ),
    url(r'^$', index),
    url(r'^about/', about),
)


