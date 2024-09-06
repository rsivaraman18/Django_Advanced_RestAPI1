from . models import *
from rest_framework import serializers

# Function validator for description length
def description_length(value):
    if len(value) < 5:
        raise serializers.ValidationError('Description should be more than 5 characters')


class Mymovie_serializer(serializers.Serializer):
    id          = serializers.IntegerField(read_only = True)
    name        = serializers.CharField()
    description = serializers.CharField(validators=[description_length])
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
    
    """
    Validation can be Done in 3 Types.
    VALIDATION NOT MANDATORY ,If need we can do that.
    Type1 : Field Based Validataion syntax -> def validate_name(self,value):
    Type2 : Object Based Validation
    Type3 : Function Validators
    Either of one type can be used or combine together also used.
    """
    
    # Object-based validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and Description should be unique')
        return data
    
    ## Field based Validation for name
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError('Name should be more than 3 characters')
        else:
            return value
  
   