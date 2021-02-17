# i can remove these first 2 lines as not using them right now
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from account.models import Account


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
