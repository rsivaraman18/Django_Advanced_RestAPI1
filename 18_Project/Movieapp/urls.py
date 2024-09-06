from django.contrib import admin
from django.urls import path,include
from . views import *


urlpatterns = [
   # path('reviews/',                    ReviewAll.as_view()) ,
   # path('reviews/<int:pk>/',           ReviewbyId.as_view()) ,
   # path('add_reviews/<int:pk>/',       AddNewReviewtoWatchlist.as_view()) ,

   ### NEW REVIEW
   path('watch/<int:pk>/review_create/',  AddNewReviewtoWatchlist.as_view()),
   path('watch/show_reviews/',            ReviewAll.as_view()),
   path('watch/<int:pk>/review_detail/',  ReviewbyId.as_view()),







]



"""
NEW URLS
http://127.0.0.1:8000/movieapi/watch/<int:pk/review_create/>
http://127.0.0.1:8000/movieapi/watch/<int:pk/review_view/>

#### OLDGENERICVIEWSET

http://127.0.0.1:8000/movieapi/reviews/
http://127.0.0.1:8000/movieapi/reviews/1/
http://127.0.0.1:8000/movieapi/add_reviews/1/

"""


