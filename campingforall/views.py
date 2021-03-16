# i can remove these first 2 lines as not using them right now
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from account.models import Account
from django.conf import settings
from django.conf.urls.static import static
from destination.models import BlogPost
from operator import attrgetter


def index(request):
    context = {}
    campsites = sorted(BlogPost.objects.all(), key=attrgetter('date_updated'),reverse=True)
    context['campsites'] = campsites

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    