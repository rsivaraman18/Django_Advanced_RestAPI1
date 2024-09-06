from django.contrib import admin
from django.urls import path,include
from . views import *


##### FOR ROUTERS
from rest_framework import viewsets

from rest_framework.routers import DefaultRouter
router = DefaultRouter() 
router.register('generic_stream',          RouterStream , basename='streamplatform')
router.register('modelviewset_watchlist',  Watchlist_MVS, basename='watchlist')
router.register('GV_reviews', Reviews_Views, basename='review')

urlpatterns = [
   path('',include(router.urls)),

   path('reviews/',                    ReviewAll.as_view()) ,
   path('reviews/<int:pk>/',           ReviewbyId.as_view()) ,
   ## 1 User can Put 1 review Only
   path('add_reviews/<int:pk>/',       AddNewReviewtoWatchlist.as_view()) ,
]


""" 

#### GENERICVIEWSET
http://127.0.0.1:8000/movieapi/generic_stream/
http://127.0.0.1:8000/movieapi/generic_stream/2/

#### MODEL VIEWSET
http://127.0.0.1:8000/movieapi/modelviewset_watchlist/
http://127.0.0.1:8000/movieapi/modelviewset_watchlist/1/

#### MODELREAADONLY DATASET
http://127.0.0.1:8000/movieapi/modelreadviewset_review/
http://127.0.0.1:8000/movieapi/modelreadviewset_review/1/

"""


"""
http://127.0.0.1:8000/movieapi/add_reviews/1/
"""