
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from content.models import Article


def index(request):
    return render(request , '404.html')
    

def content(request, content_slug):
    art = Article.objects.filter(slug=content_slug)
    return render(request , 'blog.html' , {'name':art[0].name , 'text':art[0].text})

def content(request, content_slug):
    art = Article.objects.filter(slug=content_slug)
    return render(request , 'blog.html' , {'name':art[0].name , 'text':art[0].text})

def content(request, content_slug):
    art = Article.objects.filter(slug=content_slug)
    return render(request , 'blog.html' , {'name':art[0].name , 'text':art[0].text})

def index(request):
   return render(request , 'index.html')
    
 
 
def index(request):
   return render(request , 'index.html')
    
 
 
