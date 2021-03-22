from django.shortcuts import render, get_object_or_404
from .models import Googlemap
from .forms import GooglemapModelForm
from geopy.geocoders import Nominatim
from .utils import get_geo
from geopy.distance import geodesic
import folium

# Create your views here.

def Calc_dist_view(request):
    obj = get_object_or_404(Googlemap, id=1)
    form = GooglemapModelForm(request.POST or None)
    geolocator = Nominatim(user_agent='googlemap')

    ip = '108.130.52.184'
    country, city, lat, lon = get_geo(ip)
    # print('location country', country)
    # print('location city', city)
    # print('location lat, lon', lat, lon)

    location = geolocator.geocode(city)
    # print('###', location)

    l_lat = lat
    l_lon = lon
    pointA = (l_lat, l_lon)

    # use of folium map
    m = folium.Map(width=900, height=500, location=pointA)

    if form.is_valid():
        instance = form.save(commit=False)
        dest_ = form.cleaned_data.get('dest')
        dest = geolocator.geocode(dest_)
        # print(dest)
        d_lat = dest.latitude
        d_lon = dest.longitude

        pointB = (d_lat, d_lon)

        distance = round(geodesic(pointA, pointB).km, 2)

        instance.location = location
        instance.distance = distance
        instance.save()
    # passing folium in html representation
    m = m._repr_html_()

    context = {
        'distance' : obj,
        'form' : form,
        'map': m,
    }

    return render(request, 'map/map.html', context)