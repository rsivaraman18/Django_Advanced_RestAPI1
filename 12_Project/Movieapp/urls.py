
from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
   ### NORMAL API VIEWS
   # WATCHLIST 
   path('watchlist/',          Watchlist.as_view()) ,
   path('watchlist/<int:id>/', Watchlistbyid.as_view()) ,
   # path('watchlist/<int:id>/reviewinfo/', Watchlistbyid.as_view()) ,

  
   # #### MIXINS GENRIC VIEWS
   # # Reviews
   # path('reviews/',          Review.as_view()) ,
   # path('reviews/<int:pk>/', Reviewbyid.as_view()) ,


    #### GENRIC VIEWS
   #### Reviews Model
   path('reviews/',                    ReviewAll.as_view()) ,
   path('reviews/<int:pk>/',           ReviewbyId.as_view()) ,
   path('reviews/watchlist/<int:pk>/', ReviewbyWatchlist.as_view()) ,
   path('reviews/rating/<int:pk>/',    ReviewbyRating.as_view()) ,
   ### THIS URL NOT WORKING
   path('reviews/addreviewtowatchlist/<int:id>/',    AddNewReviewtoWatchlist.as_view()) ,




   ####### GENERIC VIEWS
   # Stream Platform
   path('stream/',          Stream.as_view()) ,
   path('stream/<int:pk>/', Streambyid.as_view()) ,
   path('stream/<int:pk>/watchlist/', StreamWatchDetails.as_view()) ,



]


""" 
WEB URLS --->
http://127.0.0.1:8000/movieapi/watchlist/
http://127.0.0.1:8000/movieapi/watchlist/1/
http://127.0.0.1:8000/movieapi/stream/
http://127.0.0.1:8000/movieapi/stream/1/
http://127.0.0.1:8000/movieapi/reviews/
http://127.0.0.1:8000/movieapi/reviews/1/


POST --http://127.0.0.1:8000/movieapi/reviews/
 {
   "rating": 1,
   "description": "Best Ever",
   "active": true,       
   "watchlist": 1        
 }

 
####### 
GENERIC VIEWS 
1  INPUT: {
            "id": 4,
            "watchdetails": [],
            "name": "ee",
            "about": "ee",
            "website": "https://www.eee.com/"
            }
   URL: http://127.0.0.1:8000/movieapi/platform/

2 INPUT : 



"""
