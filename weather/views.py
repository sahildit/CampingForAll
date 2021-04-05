from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib.request
import json


# Create your views here.
def weatherview(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=80c0a759d9c19b4d4f93903eb4bb0c0e').read()
        tempvar = json.loads(source)

        data = {
            "temp": str(tempvar['main']['temp']) + ' °C',
            "pressure": str(tempvar['main']['pressure']),
            "humidity": str(tempvar['main']['humidity']),
            'main': str(tempvar['weather'][0]['main']),
            'description': str(tempvar['weather'][0]['description']),
            'icon': tempvar['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}


       
    return render(request, 'weather/weather.html',data)
