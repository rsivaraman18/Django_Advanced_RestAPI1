from .models import *
from rest_framework import serializers


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyStreamPlatform
        fields = '__all__'   



class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWatchlist
        fields = '__all__'  
       







