from django.urls import path
from .views import weatherview
from . import views

app_name = 'weather'

urlpatterns = [
    path('weather/', views.weatherview, name='weatherview'),
]