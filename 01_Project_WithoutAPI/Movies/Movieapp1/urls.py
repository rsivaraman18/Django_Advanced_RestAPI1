
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movies_list/',            views.movie_list),
    path('movies_list/<int:id>/',   views.movie_listbyid),
    path('movies_create/',          views.movies_create),
    path('movies_update/',          views.movie_update),
]