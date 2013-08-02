from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from product.views import *

urlpatterns = patterns('',
    url(r'^$',ItemIndex),
    url(r'^item/edit/(?P<content_slug>\w+)/$',edit),
   	url(r'^item/view/(?P<content_slug>\w+)/$',view),
    url(r'^item/analytics',analytics),
    url(r'^item/create',add),
    url(r'^item/delete/(?P<content_slug>\w+)/$',remove),

)



