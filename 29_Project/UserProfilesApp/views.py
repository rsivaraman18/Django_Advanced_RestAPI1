from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from UserProfilesApp.serializers import *
from UserProfilesApp.models import *


"""
1.REGISTER --> When a New User Register New Token Will Be Generated.
2.LOGOUT   --> On Logout the User Token will be Deleted.
"""

@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        uservalues = request.data
        serializer = RegistrationSerializer(data=uservalues)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successfully !!!"
            data['username'] = account.username
            data['email']    = account.email
            token = Token.objects.get(user=account).key
            print('Token : ',token)
            data['token'] = token
            
        else:
            data = serializer.errors
        
        return Response(data,status.HTTP_201_CREATED)
    



@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'message':f'{request.user.username} User Token Deleted Successfully'},status=status.HTTP_200_OK) 














