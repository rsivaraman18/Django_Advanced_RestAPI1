from django.contrib import admin
from django.urls import path,include
from . views import *





urlpatterns = [
   ###  REVIEWS --> Create,Update,View All,Detail Id View
   path('movie/showall_reviews/',            ReviewAll.as_view()),
   path('movie/<int:pk>/review_create/',     AddNewReviewtoWatchlist.as_view()),
   path('movie/<int:pk>/review_detail/',     ReviewbyId.as_view()),
   # path('movie/<int:pk>/review_update/',  UpdateReviewView.as_view()),


   ### STREAMS --> Create,Viewall,Detail ID View,Delete
   path('stream/showall_createstream/',              StreamPlatform.as_view()),
   path('stream/<int:id>/detailview_updatestream/',  StreamPlatformbyID.as_view()),



   ### WATCHLIST -->
   path('watchlist/showall_createwatchlist/',             Watchlist.as_view()) ,
   path('watchlist/<int:id>/detailview_updatewatchlist/', Watchlistbyid.as_view()) ,


]

"""
Detailed Url/Method Information are created and provided in Excel Sheet.
Please Follow the Excel Sheet.
"""







