
from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
   path('watchlist/',          Watchlist.as_view()) ,
   path('watchlist/<int:id>/', Watchlistbyid.as_view()) ,

   # Platform
   path('platform/',          Stream.as_view()) ,
   path('platform/<int:id>/', Streambyid.as_view()) ,

   # Reviews
   path('reviews/',          Review.as_view()) ,
   path('reviews/<int:id>/', Reviewbyid.as_view()) ,


]

""" WEB URLS
http://127.0.0.1:8000/movieapi/watchlist/
http://127.0.0.1:8000/movieapi/watchlist/1/
http://127.0.0.1:8000/movieapi/platform/
http://127.0.0.1:8000/movieapi/platform/1/
http://127.0.0.1:8000/movieapi/reviews/
http://127.0.0.1:8000/movieapi/reviews/1/

"""
