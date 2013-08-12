from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model


def Index(request):
	return render(request , '404.html')

def ProfileView(request):
	return render(request , 'profile/view.html')

def ProfileEdit(request):
    return render(request , 'profile/edit.html')

