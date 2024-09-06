from rest_framework .views import  APIView
from rest_framework . response import Response
from rest_framework import status
from .serializers import *
from . models import *
###

        































##### STREAM CLASS VIEW

class Stream(APIView):
    def get(self,request):
        platform          = MyStreamPlatform.objects.all()
        serial_platform   = StreamPlatformSerializer(platform,many=True)
        return Response(serial_platform.data)
    
    def post(self,request):
        user = request.data
        serial_data = StreamPlatformSerializer(data=user)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors)
        


class Streambyid(APIView):
    def get(self,request,id):
        movie        =  MyStreamPlatform.objects.get(id=id)
        serial_movies = StreamPlatformSerializer(movie)
        return Response(serial_movies.data)
    
    ## PUT --> Update the Entire Object
    def put(self,request,id):
        user = request.data
        movie = MyStreamPlatform.objects.get(id=id)
        serial_data = StreamPlatformSerializer(movie,data=user,)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)

    ## Validation Panna Field Compulsory Vennum
    def patch(self,request,id):
        user = request.data
        movie = MyStreamPlatform.objects.get(id=id)
        serial_data = StreamPlatformSerializer(movie,data=user,partial=True)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

    def delete(self,request,id):
        movie = MyStreamPlatform.objects.get(id=id)
        movie.delete()
        content = {'msg':  f'Movie - {id} Deleted'}
        return Response(content,status=status.HTTP_204_NO_CONTENT) 



########## WATCH LIST 


class Watchlist(APIView):

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
        
    



class Watchlistbyid(APIView):
    def get(self,request,id):
        movie        = MyWatchlist.objects.get(id=id)
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

##################

# REVIEW CLASS VIEW


class Review(APIView):

    def get(self,request):
        movies        = MyReview.objects.all()
        serial_movies = ReviewSerializer(movies,many=True)
        return Response(serial_movies.data)
    
    def post(self,request):
        user = request.data
        serial_data = ReviewSerializer(data=user)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors)
        



class Reviewbyid(APIView):
    def get(self,request,id):
        movie        = MyReview.objects.get(id=id)
        serial_movies = ReviewSerializer(movie)
        return Response(serial_movies.data)
    
    ## PUT --> Update the Entire Object
    def put(self,request,id):
        user = request.data
        movie = MyReview.objects.get(id=id)
        serial_data = ReviewSerializer(movie,data=user,)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)

    ## Validation Panna Field Compulsory Vennum
    def patch(self,request,id):
        user = request.data
        movie = MyReview.objects.get(id=id)
        serial_data = ReviewSerializer(movie,data=user,partial=True)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

    def delete(self,request,id):
        movie = MyReview.objects.get(id=id)
        movie.delete()
        content = {'msg':  f'Movie - {id} Deleted'}
        return Response(content,status=status.HTTP_204_NO_CONTENT) 
