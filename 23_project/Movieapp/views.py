from django.forms import ValidationError
from rest_framework .views import  APIView
from rest_framework . response import Response
from rest_framework import status
from .serializers import *
from . models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from.permission import *



####################################################################
################## REVIEWS CREATED ON WATCHLIST BY USER ############


# SHOW ALL REVIEWS 
# http://127.0.0.1:8000/movieapi/movie/show_reviews/

class ReviewAll(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticated]  
    queryset         = MyReview.objects.all()
    serializer_class = ReviewSerializer1

###################################################################



# Only Admin Can Edit any review where others can edit his own.
# SHOW Review ID Details -- Review ID
# GET --> http://127.0.0.1:8000/movieapi/movie/1/review_detail/
# PUT --> http://127.0.0.1:8000/movieapi/movie/1/review_detail/

class ReviewbyId(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsReviewUserorReadOnlyorStaff] 
    queryset         = MyReview.objects.all()
    serializer_class = ReviewSerializer1


#####################################################################




# Create New Review to a Movie(Watchlist)--1 user --1 Review --1Movie
# http://127.0.0.1:8000/movieapi/movie/1/review_create/

from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import MyWatchlist, MyReview
from .serializers import ReviewSerializer1

class AddNewReviewtoWatchlist(generics.CreateAPIView):
    serializer_class = ReviewSerializer1
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        return MyReview.objects.all()  # Provide a queryset for the view

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        data1 = MyWatchlist.objects.get(pk=pk) 
        
        reviewer_name = self.request.user
        review_queryset = MyReview.objects.filter(watchlist=data1, reviewer_name=reviewer_name)
        if review_queryset.exists():
            raise ValidationError('You have Already Registered')

        if data1.number_rating == 0:
            data1.avg_rating = serializer.validated_data['rating']  
        else:
            avg_cal = (   (data1.avg_rating * data1.number_rating) + (serializer.validated_data['rating'])   )  /(data1.number_rating+1)
            data1.avg_rating = round(avg_cal,3)
        
        data1.number_rating = data1.number_rating + 1
        data1.save()
        serializer.save(watchlist=data1, reviewer_name=reviewer_name)

######################################################################



#######################  REVIEW ENDS HERE    #################################



################### STREAM PLATFORM  ##########


class StreamPlatform(APIView):
    permission_classes = [IsAdminOrReadonly]

    def get(self,request):
        platform          = MyStreamPlatform.objects.all()
        serial_platform   = StreamPlatformSerializer(platform,many=True,context={'request':request})
        return Response(serial_platform.data)
    
    def post(self,request):
        user = request.data
        serial_data = StreamPlatformSerializer(data=user)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors)
        


class StreamPlatformbyID(APIView):
    permission_classes = [IsAdminOrReadonly]

    def get(self,request,id):
        try:
            platform = MyStreamPlatform.objects.get(id=id)
        except MyStreamPlatform.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serial_platform = StreamPlatformSerializer(platform,context={'request':request})
        return Response(serial_platform.data)
    
    ## PUT --> Update the Entire Object
    def put(self,request,id):
        user        = request.data
        platform    = MyStreamPlatform.objects.get(id=id)
        serial_data = StreamPlatformSerializer(platform,data=user,)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)

    ## Validation Panna Field Compulsory Vennum
    def patch(self,request,id):
        user = request.data
        platform = MyStreamPlatform.objects.get(id=id)
        serial_data = StreamPlatformSerializer(platform,data=user,partial=True)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

    def delete(self,request,id):
        platform = MyStreamPlatform.objects.get(id=id)
        platform.delete()
        content = {'msg':  f'Stream - {id} Deleted'}
        return Response(content,status=status.HTTP_204_NO_CONTENT) 























##################### WATCHLIST #######################

##### CLASS BASED VIEWALl , Create --> APIVIEW USING FOR WATCHLIST
# Theme : Only Admin can edit(put,patch,delete) ,others only can view(get)

class Watchlist(APIView):
    permission_classes = [IsAdminOrReadonly] 
    def get(self,request):
        movies        = MyWatchlist.objects.all()
        serial_movies = WatchlistSerializer(movies,many=True)
        return Response(serial_movies.data)
    
    def post(self,request):
        user = request.data
        serial_data = WatchlistSerializer(data=user)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors)
        
###########################################################################        
    
#### WATCHLIST -->GETBYID
### Theme : Only Admin can edit(put,patch,delete) ,others only can view(get)

class Watchlistbyid(APIView):
    permission_classes = [IsAdminOrReadonly] 
    def get(self,request,id):
        try:
            movie        = MyWatchlist.objects.get(id=id)
        except MyWatchlist.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serial_movies = WatchlistSerializer(movie)
        return Response(serial_movies.data)
    


    ## PUT --> Update the Entire Object
    def put(self,request,id):
        user = request.data
        movie = MyWatchlist.objects.get(id=id)
        serial_data = WatchlistSerializer(movie,data=user,)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)

    ## Validation Panna Field Compulsory Vennum
    def patch(self,request,id):
        user = request.data
        movie = MyWatchlist.objects.get(id=id)
        serial_data = WatchlistSerializer(movie,data=user,partial=True)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

    def delete(self,request,id):
        movie = MyWatchlist.objects.get(id=id)
        movie.delete()
        content = {'msg':  f'Movie - {id} Deleted'}
        return Response(content,status=status.HTTP_204_NO_CONTENT) 

#####################################################################










