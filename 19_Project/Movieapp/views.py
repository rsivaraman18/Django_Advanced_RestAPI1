# from django.forms import ValidationError
# from rest_framework .views import  APIView
# from rest_framework . response import Response
# from rest_framework import status
# from .serializers import *
# from . models import *
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics
# ### Custom Permissions.py
# from.permission import *

################# NEW CODES ################

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import *
from . models import *



@api_view(['POST'])
def logout_view(request):
    pass




@api_view(['POST'])
def registration_view(request):
    pass
























