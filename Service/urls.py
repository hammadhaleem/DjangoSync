from django.conf.urls import patterns, include, url
from Service.views import *
from content.views import *
from product.views import *
from django.contrib import admin
from Service.admin import user_admin_site
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Service.views.home', name='home'),
    # url(r'^Service/', include('Service.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^thread/(?P<thread_id>\d+)/$' , include ('discussion.urls'))
    # Uncomment the next line to enable the admin:
    
   
    url(r'^$', index),    
    url(r'^faq/',faq),    
    url(r'^about/', about),
    url(r'^inventory/',inventory),
    url(r'^category/',category),
    url(r'^content/(?P<content_slug>\w+)/$',content  ),
    (r'^item/',include('product.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^user/', include(user_admin_site.urls)),
    #url(r'^', include('myapp.urls')),
)



