from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email' , 'password' , 'password2']
        extra_kwargs =  {
                            'password': {'write_only' : True}
                        }
        
    
    def save(self):
        user_name       = self._validated_data['username']
        user_email      = self._validated_data['email']
        user_password   = self._validated_data['password']
        user_password2  = self._validated_data['password2']

        if user_password != user_password2:
            raise serializers.ValidationError({'Error':'Password1 & Password Doesnot Match'})
        
        if User.objects.filter(email=user_email).exists():
            raise serializers.ValidationError({'Error': 'Email Already Exists'})
        
        account = User(email=user_email,username = user_name)
        account.set_password(user_password)
        account.save()
        return account
    
