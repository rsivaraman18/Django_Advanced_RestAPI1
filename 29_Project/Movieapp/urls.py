from django.contrib import admin
from django.urls import path,include
from . views import *



urlpatterns = [
   ### WATCHLIST URLS --> CREATED BY API VIEW















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

   # PROJECT- 26 & 27 --> Filtering 
   path('reviews/<str:username>/', UserReviewsfilter1.as_view()) ,
   path('reviews/',                UserReviewsfilter2.as_view()) ,
   path('<int:pk>/allreviews/',    UserReviewsfilter3.as_view()) ,
   path('allwatchlist/',           Watchlistfilter4.as_view()) ,

   # PROJECT- 26 & 27 --> Searching & Ordering
   path('allwatchlist_search/',           Watchlistsearch1.as_view()) ,
   path('allwatchlist_startswithsearch/', Watchlistsearch2.as_view()) ,
   path('allwatchlist_ordering/',         Watchlistorder1.as_view()) ,

   # PROJECT 28 --> PAGINATION
   path('watchlist_paginationview/',         watchlist_paginationview1.as_view()) ,
   path('watchlist_limitpaginationview/',    watchlist_limitpaginationview.as_view()) ,
   path('watchlist_cursorpagination/',       watchlist_cursorpagination.as_view()) ,
   




 

]

"""
Detailed Url/Method Information are created and provided in Excel Sheet.
Please Follow the Excel Sheet.
"""







