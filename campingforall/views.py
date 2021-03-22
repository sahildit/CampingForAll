# i can remove these first 2 lines as not using them right now
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from account.models import Account
from django.conf import settings
from django.conf.urls.static import static
from destination.models import BlogPost
from operator import attrgetter

from destination.views import destination_queryset
from googlemap.views import Calc_dist_view
# destination import destination_queryset

def index(request):
    context = {}

#  used for searching in the home screen
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    campsites = sorted(destination_queryset(query), key=attrgetter('date_updated'),reverse=True)
    context['campsites'] = campsites

    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
    