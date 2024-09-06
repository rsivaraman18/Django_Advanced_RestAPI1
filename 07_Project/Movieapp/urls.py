
from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
   path('movie/',          Movieslist.as_view()) ,
   path('movie/<int:id>/', Moviesbyid.as_view()) ,
]
