
from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
   path('watchlist/',          Watchlist.as_view()) ,
   path('watchlist/<int:id>/', Watchlistbyid.as_view()) ,

   # Platform
   path('platform/',          Stream.as_view()) ,
   path('platform/<int:id>/', Streambyid.as_view()) ,

]
