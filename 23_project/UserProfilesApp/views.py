from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from UserProfilesApp.serializers import *
# from UserProfilesApp.models import *
from rest_framework_simplejwt.tokens import RefreshToken



# New User Registration and Token Generation Automatically

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

            ### JWT
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }

        else:
            data = serializer.errors
        
        return Response(data)
    




'''This logout is to delete a User token'''

@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'message':f'{request.user.username} Token Deleted Successfully'},status=status.HTTP_200_OK) 






















# ### GENERAL METHOD -- NEW USER REGISTRATION
# @api_view(['POST',])
# def registration_view(request):

#     if request.method == 'POST':
#         uservalues = request.data
#         serializer = RegistrationSerializer(data=uservalues)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


        

        


