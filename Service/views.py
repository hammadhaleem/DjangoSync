from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model

from content.models import *
from product.models import *



def about(request):
	return render(request , 'about.html')

def index(request):
    ite =item.objects.all()
    return render(request , 'index.html' ,  {'ite':ite })
    
def faq (request) :
	return render(request , 'faq.html' )

def content(request, content_slug):
    art = Article.objects.filter(slug=content_slug)
    return render(request , 'blog.html' , {'name':art[0].name , 'text':art[0].text})

def inventory(request):
	ite =item.objects.all()
	cat =category.objects.all()
	return render(request , 'inventory.html' , {'ite':ite ,'cat':cat } )
