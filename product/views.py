from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from content.models import Article


def ItemIndex(request):
    return render(request , '404.html')

def edit(request, content_slug):
    art = Article.objects.filter(slug=content_slug)
    return render(request , 'blog.html' , {'name':art[0].name , 'text':art[0].text})

def view(request, content_slug):
    art = Article.objects.filter(slug=content_slug)
    return render(request , 'blog.html' , {'name':art[0].name , 'text':art[0].text})

def remove(request, content_slug):
    art = Article.objects.filter(slug=content_slug)
    return render(request , 'blog.html' , {'name':art[0].name , 'text':art[0].text})

def analytics(request):
   return render(request , 'index.html')
    
def add(request):
   return render(request , 'index.html')
    
 
 
