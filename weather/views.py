from django.shortcuts import render
from django.http import HttpResponse
import requests


# Create your views here.

def get_google_data(city):
    

        # reference for below code - https://github.com/akjasim/cb_dj_weather_app

        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        LANGUAGE = "en-US,en;q=0.5"
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE

        # replacing spacing between names of city with the '+' so that it can fetch them all
        city = city.replace(' ', '+')
        google_data = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
        return google_data


def weatherview(request):
    data = None

    # done with the help of google web scrapper where i will be scraping weather from real-time google weathe board
    # use of third party libraries such as requests and beautifulsoup4 - which is a python library
    # so first we'll make the url and then scape the data from google weather board.
    if 'city' in request.GET:
        city = request.GET.get('city')
        google_data = get_google_data(city)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(google_data, 'html.parser')


        data = dict()

        data['country'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
        data['daytime'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
        # data['status'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
        # data['temperature'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text       

       
    return render(request, 'weather/weather.html', {'weather': data})
