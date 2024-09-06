from rest_framework .views import  APIView
from rest_framework . response import Response
from rest_framework import status
from .serializers import *
from . models import *
from rest_framework import mixins
from rest_framework import generics



#######################################################
##### CLASS BASED VIEW  --> APIVIEW USING FOR WATCHLIST

#### WATCHLIST
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
        
###########################################################################        
    
#### WATCHLIST -->GETBYID
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


#######################################################################



# ##################################################################
# ##################################################################
# # REVIEW CLASS VIEW --> CREATED USING USING GENERIC-MIXINS
# ### queryset and serializer_class are attribute of mixins we cannot change them
# from rest_framework import mixins
# from rest_framework import generics

# #### REVIEW
# class Review(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset         = MyReview.objects.all()  
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# ### REVIEW BY ID
# class Reviewbyid(mixins.RetrieveModelMixin ,mixins.UpdateModelMixin,
#                 mixins.DestroyModelMixin,  generics.GenericAPIView):
    
#     queryset         = MyReview.objects.all()  
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# ########################################################################
# ########################################################################

##### REVIEWS IN GENERIC VIEWS

from rest_framework import generics

#### REVIEW GENERIC PLATFORM 
class ReviewAll(generics.ListCreateAPIView):
    queryset         = MyReview.objects.all()
    serializer_class = ReviewSerializer


#### REVIEW GENERIC BY ID
class ReviewbyId(generics.RetrieveUpdateDestroyAPIView):
    queryset         = MyReview.objects.all()
    serializer_class = ReviewSerializer


#### FILTER REVIEW BASED ON WATCHLIST-NO 
## ONLY GET METHOD,Allowed, IF you need POST add this below (generics.ListCreateAPIView)
class ReviewbyWatchlist(generics.ListAPIView): 
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        data = MyReview.objects.filter(watchlist=pk)
        return data


#### FILTER REVIEW BASED ON RATING-VALUE 
## ONLY GET METHOD,Allowed, IF you need POST add this below (generics.ListCreateAPIView)
class ReviewbyRating(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        data = MyReview.objects.filter(rating=pk)
        return data
    

#######################################################
#######################################################
class AddNewReviewtoWatchlist(generics.CreateAPIView): #only Post method
    serializer_class = ReviewSerializer1

    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        data = MyWatchlist.objects.filter(pk=pk)
        serializer.save(Watchlist=data)
        


########################################################
########################################################





























####### NOW --->GENERIC VIEW CLASS
#### FOR STREAM
from rest_framework import generics

##STREAM PLATFORM 
class Stream(generics.ListCreateAPIView):
    queryset         = MyStreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

### STREAM PLATFORM BY ID
class Streambyid(generics.RetrieveUpdateDestroyAPIView):
    queryset         = MyStreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
















