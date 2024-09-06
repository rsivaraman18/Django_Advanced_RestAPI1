
from rest_framework .views import  APIView
from rest_framework . response import Response
from rest_framework import status
from .serializers import *


class Movieslist(APIView):

    def get(self,request):
        movies        = Mymovies.objects.all()
        serial_movies = Mymovie_serializer(movies,many=True)
        return Response(serial_movies.data)
    
    def post(self,request):
        user = request.data
        serial_data = Mymovie_serializer(data=user)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors)
        
    



 

class Moviesbyid(APIView):
    def get(self,request,id):
        movie        = Mymovies.objects.get(id=id)
        serial_movies = Mymovie_serializer(movie)
        return Response(serial_movies.data)
    
    ## PUT --> Update the Entire Object
    def put(self,request,id):
        user = request.data
        movie = Mymovies.objects.get(id=id)
        serial_data = Mymovie_serializer(movie,data=user,)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)

    ## Validation Panna Field Compulsory Vennum
    def patch(self,request,id):
        user = request.data
        movie = Mymovies.objects.get(id=id)
        serial_data = Mymovie_serializer(movie,data=user,partial=True)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

    def delete(self,request,id):
        movie = Mymovies.objects.get(id=id)
        movie.delete()
        content = {'msg':  f'Movie - {id} Deleted'}
        return Response(content,status=status.HTTP_204_NO_CONTENT) 

