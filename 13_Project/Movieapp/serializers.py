from .models import *
from rest_framework import serializers

"""
Nested Serializer going to Implement Here.
1 Movie can have 1 Platform
1 Platform can have many Movies

1 Review for 1 movie
1 movie can have many review

"""
### TO CREATE A NEW RATIONG FOR MOVIE WITHOUT ADDING WATCHLIST NUMBER
class ReviewSerializer1(serializers.ModelSerializer):
    class Meta:
        model = MyReview
        exclude = ('watchlist',)
          




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyReview
        fields = '__all__'  


"""
Reviews is Child for Watchlist. You can view Review info in watchlist.
This detailed are collected using dested serializer :review info
"""
class WatchlistSerializer(serializers.ModelSerializer):
    reviewinfo = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = MyWatchlist
        fields = '__all__'  

"""
Watchlist is Child for StreamPlatform.You can view Watchlist info in Platform
This detailed are collected using dested serializer :watchdetails
"""
### Watchlist is Child for Platform.You can view Watchlist info in Platform
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchdetails = WatchlistSerializer(many=True,read_only=True)
    class Meta:
        model = MyStreamPlatform
        fields = '__all__'           







