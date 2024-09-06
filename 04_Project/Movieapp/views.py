from rest_framework . response import Response
from rest_framework . decorators import api_view  ## Function Based
from rest_framework import status
from . serializers import *
from . models import *



@api_view(['GET','POST'])
def movies(request):
    if request.method == "GET":
        movies        = Mymovies.objects.all()
        serial_movies = Mymovie_serializer(movies,many=True)
        return Response(serial_movies.data)
        
        
    elif request.method == "POST":
        user = request.data
        serial_data = Mymovie_serializer(data=user)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors)
        




@api_view(['GET','PUT','DELETE'])
def moviebyid(request,id):
    try:
        movie  = Mymovies.objects.get(id=id)

    except Mymovies.DoesNotExist:
        return Response({'Error':'No movie Found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        movie        = Mymovies.objects.get(id=id)
        serial_movies = Mymovie_serializer(movie)
        return Response(serial_movies.data)
    
    elif request.method =="PUT":
        user = request.data
        movie = Mymovies.objects.get(id=id)
        serial_data = Mymovie_serializer(movie,data=user,)
        if serial_data.is_valid():
            serial_data.save()
            return Response(serial_data.data)
        else:
            return Response(serial_data.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method =="DELETE":
       movie = Mymovies.objects.get(id=id)
       movie.delete()
       content = {'msg':  f'Movie - {id} Deleted'}
       return Response(content,status=status.HTTP_204_NO_CONTENT) 
    
        

