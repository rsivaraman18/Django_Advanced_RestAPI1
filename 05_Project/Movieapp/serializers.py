from . models import *
from rest_framework import serializers


class Mymovie_serializer(serializers.Serializer):
    id          = serializers.IntegerField(read_only = True)
    name        = serializers.CharField()
    description = serializers.CharField()
    active      = serializers.BooleanField()

    ### FOR POST METHOD
    def create(self,validated_data):
        return Mymovies.objects.create(**validated_data)
    
    ### FOR Update PUT METHOD
    def update(self,instance,validate_data):
        instance.name        = validate_data.get('name','Empty')
        instance.description = validate_data.get('description','Empty')
        instance.active      = validate_data.get('active','Empty')
        instance.save()
        return instance
  
   