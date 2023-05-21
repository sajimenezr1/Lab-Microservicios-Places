from django.urls import path
from django.conf.urls import  include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [

    path('places/',views.placesList, name='placesList'),
    path('createplaces/', views.createPlaces, name='createPlaces'),

]