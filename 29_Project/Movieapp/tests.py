from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from . models import *
from . serializers import *

class StreamPlatformCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example",password="mypassword@123")
        self.token = Token.objects.get(user__username =self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_streamplatform_create(self):
        data =  {
                    "name" : "Netflix",
                    "about": " Streaming Platform",
                    "website": "https://netflix.com"
                }
        response = self.client.post(reverse('StreamCreateViewall'),data)
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.post(reverse('StreamCreateViewall'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)