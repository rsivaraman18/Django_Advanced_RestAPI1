from django.forms import ValidationError
from rest_framework .views import  APIView
from rest_framework . response import Response
from rest_framework import status
from .serializers import *
from . models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
### Custom Permissions.py
from.permission import *

#### REVIEW GENERIC PLATFORM 
class ReviewAll(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]  ### Builtin Permission
    queryset         = MyReview.objects.all()
    serializer_class = ReviewSerializer1


# #### REVIEW GENERIC BY ID
class ReviewbyId(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [AdminOrReadonly] ###Custom Permission
    permission_classes = [ReviewUserorReadOnly] ###Custom Permission
    queryset         = MyReview.objects.all()
    serializer_class = ReviewSerializer



############ ADD NEW REVIEW  ################
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import MyWatchlist, MyReview
from .serializers import ReviewSerializer1

class AddNewReviewtoWatchlist(generics.CreateAPIView):
    serializer_class = ReviewSerializer1

    def get_queryset(self):
        return MyReview.objects.all()  # Provide a queryset for the view

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        print('Primary Key:', pk)  ##Key
        data1 = MyWatchlist.objects.get(pk=pk) ## Movie name
        
        reviewer_name = self.request.user
        print('reviewwer name:',reviewer_name)
        review_queryset = MyReview.objects.filter(watchlist=data1, reviewer_name=reviewer_name)
        if review_queryset.exists():
            raise ValidationError('You have Already Registered')
        
        serializer.save(watchlist=data1, reviewer_name=reviewer_name)
















