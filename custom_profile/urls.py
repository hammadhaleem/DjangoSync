from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import * 




urlpatterns = patterns('',
   
    url(r'^$', Index),    
    url(r'^view/',ProfileView),    
    url(r'^edit/', ProfileEdit),
)



