from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from product.views import *


urlpatterns = patterns('',
    url(r'^$',ItemIndex),
    url(r'^edit/(?P<content_slug>\w+)/$',edit),
   	url(r'^view/(?P<content_slug>\*+)/$',view),
    url(r'^analytics',analytics),
    url(r'^create',add),
    url(r'^delete/(?P<content_slug>\w+)/$',remove),

)



