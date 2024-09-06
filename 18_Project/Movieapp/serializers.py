from .models import *
from rest_framework import serializers

"""
Nested Serializer going to Implement Here.
1 Movie can have 1 Platform
1 Platform can have many Movies

1 Review for 1 movie
1 movie can have many review

"""
### TO CREATE A NEW RATING FOR MOVIE WITHOUT ADDING WATCHLIST NUMBER
class ReviewSerializer1(serializers.ModelSerializer):
    reviewer_name = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = MyReview
        exclude = ['watchlist']
        # fields = ['rating', 'description', 'watchlist', 'reviewer_name']
        # read_only_fields = ['watchlist', 'reviewer_name']


class WatchlistSerializer(serializers.ModelSerializer):
    reviewinfo = ReviewSerializer1(many=True,read_only=True)
    class Meta:
        model = MyWatchlist
        fields = '__all__'  


### Watchlist is Child for Platform.You can view Watchlist info in Platform
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchdetails = WatchlistSerializer(many=True,read_only=True)
    class Meta:
        model = MyStreamPlatform
        fields = '__all__'           







