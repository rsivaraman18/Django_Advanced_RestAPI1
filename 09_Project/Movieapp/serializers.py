from .models import *
from rest_framework import serializers

"""
Nested Serializer going to Implement Here.
1 Movie can have 1 Platform
1 Platform can have many Movies
"""

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWatchlist
        fields = '__all__'  



class StreamPlatformSerializer(serializers.ModelSerializer):
    watchdetails = WatchlistSerializer(many=True,read_only=True)
    class Meta:
        model = MyStreamPlatform
        fields = '__all__'           







