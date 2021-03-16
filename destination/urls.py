from django.urls import path
from destination.views import(
    
    create_destination_view,
    description_view,
)

app_name = 'destination'

urlpatterns = [
    path('create/', create_destination_view, name="create"),
    path('<slug>/', description_view, name="description"),
]