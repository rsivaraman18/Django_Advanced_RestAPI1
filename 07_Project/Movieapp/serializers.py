from .models import Mymovies
from rest_framework import serializers

class Mymovie_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Mymovies
        fields = '__all__'   # For all fields
        #fields = ['name','description']  # If you need check only specific Field and return specific
        #exclude = ['name']

    # Object-based validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and Description should be unique')
        return data
    
    # Field-based validation for name
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Name should be more than 2 characters')
        return value


    ###This Function is to return new fields without registering in database
    name_len          = serializers.SerializerMethodField()
    days_since_joined = serializers.SerializerMethodField()
    ## Return a New Calculated Value
    def get_name_len(self,object):
        length = len(object.name)
        return length 
    
    def get_days_since_joined(self,object):
        return '365 Days'

    







