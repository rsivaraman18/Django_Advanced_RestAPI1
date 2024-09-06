from django.contrib import admin
from django.urls import path,include
from . views import *


urlpatterns = [
   path('reviews/',                    ReviewAll.as_view()) ,
   path('reviews/<int:pk>/',           ReviewbyId.as_view()) ,
   path('add_reviews/<int:pk>/',       AddNewReviewtoWatchlist.as_view()) ,
]



"""
#### GENERICVIEWSET

http://127.0.0.1:8000/movieapi/reviews/
http://127.0.0.1:8000/movieapi/reviews/1/

"""


