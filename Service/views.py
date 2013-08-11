from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import auth
from django.views.generic import ListView, DetailView

from .forms import UserProfileForm

from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django import forms
from .models import UserProfile
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse

from content.models import *
from product.models import *


from django.views.generic import ListView, DetailView
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse



def about(request):
	return render(request , 'about.html')

def index(request):
    return render(request , 'index.html')
    
def faq (request) :
	return render(request , 'faq.html' )

def content(request, content_slug):
    art = Article.objects.filter(slug=content_slug)
    return render(request , 'blog.html' , {'name':art[0].name , 'text':art[0].text})

def inventory(request):
	ite =item.objects.all()
	cat =category.objects.all()
	return render(request , 'inventory.html' , {'ite':ite ,'cat':cat } )


class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={"slug": self.request.user})