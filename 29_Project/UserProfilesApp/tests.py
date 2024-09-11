from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):
    
    def test_register(self):
        data =  {
                    "username"  : "testcase" ,
                    "email"     : "testcase@gmaail.com",
                    "password"  : "password@123" ,
                    "password2" : "password@123",
                }
        response = self.client.post(reverse('UserRegister'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)



class LoginLogoutTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example",password="mypassword@123")

    def test_login(self):
        data =  {
                    "username"  : "example" ,
                    "password"  : "mypassword@123" ,
                }
        response = self.client.post(reverse('UserLogin'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username = "example")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.post(reverse('UserLogout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
