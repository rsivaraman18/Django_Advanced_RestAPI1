
from django.contrib import admin
from django.urls import path,include
from . views import *


##### FOR ROUTERS
from rest_framework import viewsets

from rest_framework.routers import DefaultRouter
router = DefaultRouter() 
router.register('generic_stream',         RouterStream , basename='streamplatform')
router.register('modelviewset_watchlist', Watchlist_MVS, basename='watchlist')
router.register('modelreadviewset_review', Reviews_MRVS, basename='review')

urlpatterns = [
   ### STREAM --> VIEWSET -->GENERICVIEWSET 1-URLENOUGH
   path('',include(router.urls)),

   ### STREAMPLATFORM -- CLASS BASED GENERIC VIEWS
   path('gen_stream/',          Stream.as_view()) ,
   path('gen_stream/<int:pk>/', Streambyid.as_view()) ,


   ### WATCHLIST -->VIEWSET -->ModelVIEWSet - 1 Url
   path('',include(router.urls)),
   ### CLASS BASED --GENERAL APIVIEWS
   # WATCHLIST 
   path('watchlist/',          Watchlist.as_view()) ,
   path('watchlist/<int:id>/', Watchlistbyid.as_view()) ,



   ### WATCHLIST -->VIEWSET -->ModelReadonlyVIEWSet - 1 Url
   path('',include(router.urls)),


   #### CLASS BASED -- CLASS BASED GENERIC VIEWS
   #### Reviews Model
   path('reviews/',                    ReviewAll.as_view()) ,
   path('reviews/<int:pk>/',           ReviewbyId.as_view()) ,
   path('reviews/watchlist/<int:pk>/', ReviewbyWatchlist.as_view()) ,
   path('reviews/rating/<int:pk>/',    ReviewbyRating.as_view()) ,
  

]


""" 
WEB URLS ---> CLASS BASED VIEWS -->GENERIC --2Urls
http://127.0.0.1:8000/movieapi/gen_stream/
http://127.0.0.1:8000/movieapi/gen_stream/1/
           GENERICVIEWSET -1 URL Both ID and General
http://127.0.0.1:8000/movieapi/generic_stream/
http://127.0.0.1:8000/movieapi/generic_stream/2/
#############################################################
### CLASS BASED --GENERAL APIVIEWS
http://127.0.0.1:8000/movieapi/watchlist/
http://127.0.0.1:8000/movieapi/watchlist/1/

#### MODEL VIEWSET
http://127.0.0.1:8000/movieapi/modelviewset_watchlist/
http://127.0.0.1:8000/movieapi/modelviewset_watchlist/1/
#############################################################

####CLASS BASED GENERIC VIEWS
http://127.0.0.1:8000/movieapi/reviews/
http://127.0.0.1:8000/movieapi/reviews/1/

#### MODELREAADONLY DATASET

http://127.0.0.1:8000/movieapi/modelreadviewset_review/
http://127.0.0.1:8000/movieapi/modelreadviewset_review/1/





1.POST A NEW USING ROUTER
INPUT :  {
            "name": "Disney",
            "about": "Disney Movies",
            "website": "http://www.netflix.com"
         }
URL :  http://127.0.0.1:8000/movieapi/generic_stream/  
METHOD : POST

2.PUT 
INPUT:  {
            "name": "Disney Plus",
            "about": "Disney Movies",
            "website": "http://www.disney.com"
         }
URL :  http://127.0.0.1:8000/movieapi/generic_stream/4/          
METHOD: PUT


3.PATCH
INPUT:  {
            "name": "Disney Plus",
            "about": "Disney Movies",
            "website": "http://www.disney.com"
         }
URL :  http://127.0.0.1:8000/movieapi/generic_stream/4/          
METHOD: PUT

"""
