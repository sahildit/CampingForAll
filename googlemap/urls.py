from django.urls import path
from .views import Calc_dist_view

app_name = 'googlemap'

urlpatterns = [
    path('googlemap/', Calc_dist_view, name='calculate-view'),
]