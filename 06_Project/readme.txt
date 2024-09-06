Class Based RestApi using Serializers --> with Validation
1.Here for serialization Serilaizer used.
2.Views wriiten on class Based.
3.It works with 4 main methods(get,post,put,delete).
4.Database used is MySQL.
5.You can create superuser --> To insert fields.
6. Here Validation were done at Serializers

VALIDATION DETAILS FOR UNDERSTANDING
Validation can be Done in 3 Types.
    VALIDATION NOT MANDATORY ,If need we can do that.
    Type1 : Field Based Validataion 
            syntax -> def validate_name(self,value):
    Type2 : Object Based Validation 
            syntax--> def validate(self, data):
    Type3 : Function Validators
            
            def description_length(value):
                if len(value) < 5:
                    raise serializers.ValidationError('Description should be more than 5 characters')

            class Mymovie_serializer(serializers.Serializer):
                description = serializers.CharField(validators=[description_length])
           
Either of one type can be used or combine together also used.

  