from django.forms import ValidationError
from rest_framework .views import  APIView
from rest_framework . response import Response
from rest_framework import status
from .serializers import *
from . models import *
### FOR MIXINS AND GENERICS
from rest_framework import mixins
from rest_framework import generics

################## VIEWSET IMPORTS
from django.shortcuts import get_object_or_404
from rest_framework import viewsets


################################################
#   STREAM PLATFORM  -->  GENERIC- VIEWSETS   
class RouterStream(viewsets.ViewSet):
    
    def list(self, request):
        queryset = MyStreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = MyStreamPlatform.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(data)
        return Response(serializer.data)
    

    
    def create(self,request):
        user = request.data
        serial_data = StreamPlatformSerializer(data=user)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors)
        
    ### PUT
    def update(self,request,pk=None):
        user = request.data
        stream = MyStreamPlatform.objects.get(id=pk)
        serial_data = StreamPlatformSerializer(stream,data=user,)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)

    ### PATCH
    def partial_update(self,request,pk=None):
        user = request.data
        movie = MyStreamPlatform.objects.get(id=pk)
        serial_data = StreamPlatformSerializer(movie,data=user,partial=True)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)
    

    ## DELETE METHOD   --pk-->Default None 
    def destroy(self,request,pk=None):
        queryset = MyStreamPlatform.objects.all()
        stream = get_object_or_404(queryset, pk=pk)
        stream.delete()
        content = {'msg':  f'Movie - {pk} Deleted'}
        return Response(content,status=status.HTTP_204_NO_CONTENT) 
    


################################################
#   STREAM PLATFORM  -->  MODELVIEWSET- VIEWSETS  

class Watchlist_MVS(viewsets.ModelViewSet):
    queryset = MyWatchlist.objects.all()
    serializer_class = WatchlistSerializer
    
#####################################################


############################################################
############################################################

##### REVIEWS IN GENERIC VIEWS
from rest_framework import generics

#### REVIEW GENERIC PLATFORM 
class ReviewAll(generics.ListCreateAPIView):
    queryset         = MyReview.objects.all()
    serializer_class = ReviewSerializer1


# #### REVIEW GENERIC BY ID
class ReviewbyId(generics.RetrieveUpdateDestroyAPIView):
    queryset         = MyReview.objects.all()
    serializer_class = ReviewSerializer



############ NEW CODE ################
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
















##################################
# REVIEWS ---> GENERICVIEWSET

class Reviews_Views(viewsets.ViewSet):
    
    def list(self, request):
        queryset = MyReview.objects.all()
        serializer = ReviewSerializer1(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = MyReview.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        serializer = ReviewSerializer1(data)
        return Response(serializer.data)
    
    def create(self,request):
        user = request.data
        serial_data = ReviewSerializer1(data=user)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors)
        
    ### PUT
    def update(self,request,pk=None):
        user = request.data
        review = MyReview.objects.get(id=pk)
        serial_data = ReviewSerializer1(review,data=user,)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)

    ### PATCH
    def partial_update(self,request,pk=None):
        user = request.data
        review = MyReview.objects.get(id=pk)
        serial_data = ReviewSerializer1(review,data=user,partial=True)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)
    

    ## DELETE METHOD   --pk-->Default None 
    def destroy(self,request,pk=None):
        queryset = MyReview.objects.all()
        review = get_object_or_404(queryset, pk=pk)
        review.delete()
        content = {'msg':  f'Movie - {pk} Deleted'}
        return Response(content,status=status.HTTP_204_NO_CONTENT) 


###################################################################






