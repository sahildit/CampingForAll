"""campingforall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from weather.views import weatherview

from . import views
from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    authenticate_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('destination/', include('destination.urls', 'destination')),
    path('authenticate', authenticate_view, name="authenticate"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('googlemap/', views.Calc_dist_view, name="googlemap"),
    path('weather/', weatherview, name="weather"),





]

# this means that if we are in development mode
# what it do is that it tells like where are our static files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

