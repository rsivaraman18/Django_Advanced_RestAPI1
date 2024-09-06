
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movies),
    path('movie/<int:id>/' , views.moviebyid)
]
