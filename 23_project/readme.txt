HERE TOKEN AUTHENTICATION DONE WITH JWT.(OPTIONAL TO LEARN)
  This part will remains separate if we dont like you can leave 
  and continue with Project22 and project24.This not affect them.

JSON WEB TOKEN
1.Large Scale Project.
2.Stateless.


Document : https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#requirements

STEPS
1.Install JWT
    pip install djangorestframework-simplejwt

2.JWT Token Authentication
    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

3. URLS CHANGE --> APP urls.py
    
urlpatterns = [
    #### JWT TOKEN AUTHENTICATION
    path('api/token/',         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]

4.Makemigrations,migrate.
5.Create superuser --> make some entries in table.
6.Generating JWT TOKEN
6a.POSTMAN Application
    URL:     http://127.0.0.1:8000/userprofiles/api/token/
    METHOD:  POST
    HEADERS: --
    BODY:   Form Data
             username : siva
             password : siva
    OUTPUT: {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTQyODg3OCwiaWF0IjoxNzI1MzQyNDc4LCJqdGkiOiJkZWIxOWFkOGQ5M2U0ZDExYjVhYzczYmY2N2FjNzQzNCIsInVzZXJfaWQiOjF9.FtXK7Xhd5als4fTgwzscHxmhNUaVAnso0ndut2uIzq8",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MzQyNzc4LCJpYXQiOjE3MjUzNDI0NzgsImp0aSI6ImM2ODg3M2FjNjk1NTQwYWNhNDQ5YzgwOGQ2YzU4ZjM0IiwidXNlcl9pZCI6MX0.pzJTb3PUG8tJ2gS4SpUbksJOsKkuJ5S8bxKgiyhQ6_c"
            }
7.Check token Working (Access Token only valid for 5 mins)
    URL:     http://127.0.0.1:8000/movieapi/movie/1/review_detail/
    METHOD:  PUT
    HEADERS: AUTHORIZATION : Bearer AccesstokeneyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MzQzMTcyLCJpYXQiOjE3MjUzNDI4NzIsImp0aSI6IjM3N2ZmNjgzNjU4YzQ3YTNiMDc1Y2VlMTg4MzgzODRkIiwidXNlcl9pZCI6MX0.NKTHuzRTOklUQ20qzbPcKl7Vm53tkIWXaVgyRzzUXiA
    BODY:   Form Data {"rating":5}
            
    OUTPUT: {
            "id": 1,
            "reviewer_name": "siva",
            "rating": 5,
            "description": "Very Good",
            "active": true,
            "created": "2024-09-03T05:44:30.818282Z",
            "update": "2024-09-03T05:55:45.307172Z"
        }

8.In case Access Token expired you can get using refresh token
    URL:     http://127.0.0.1:8000/userprofiles/api/token/refresh/
    METHOD:  POST
    HEADERS: ----
    BODY:   x.www.formul encoded 
            refresh : refreshcode
            
    OUTPUT: {
                "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MzQzNzIzLCJpYXQiOjE3MjUzNDI4NzIsImp0aSI6ImQ5MmVjMjE1YjBiNzRhMjNhZDRiNWRlNWJiMDk4ODdlIiwidXNlcl9pZCI6MX0.KVpEb9ANAX6nnEJuvUnhL8wt_je_2PQwZ24xbqKg5Po"
            }

9.In case u need new refresh token everytime try this.
    9a.settings file -->
        SIMPLE_JWT = {
                'ROTATE_REFRESH_TOKENS' : True,
            }

    9b. New Refresh and Access Token Generated 
        URL:     http://127.0.0.1:8000/userprofiles/api/token/refresh/
        METHOD:  POST
        HEADERS: ----
        BODY:   x.www.formul encoded 
                refresh : refreshcode
                
        OUTPUT: {
                    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MzQ0MTg4LCJpYXQiOjE3MjUzNDI4NzIsImp0aSI6IjEwOGM5N2E0OGVhOTQ2Mjk4OTk0ZGM0OTExMjllZGFiIiwidXNlcl9pZCI6MX0.Qt0t-UACDbnh2vElxh9t5N4ApGPwLgC8pnDLeiTD-XY",
                    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTQzMDI4OCwiaWF0IjoxNzI1MzQzODg4LCJqdGkiOiJhZTY2YWFmOThkZDQ0MTMxYWRiMGQ2YWMxOGNjMWE4NCIsInVzZXJfaWQiOjF9.CwhwAz_05PXuLv1lsmyPbSQCdeYXDo3S85hEoCwzpS8"
                }

10.Now lets Do this JWT Authentication on User Registration
   as we done with Django Tokens.Whenever user register new 
   token will be Generated.

   10A.Userapp -->views.py
       Changes Made given;
       # from UserProfilesApp.models import *
       from rest_framework_simplejwt.tokens import RefreshToken
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
    10B.
        URL:     http://127.0.0.1:8000/userprofiles/register/
            METHOD:  POST
            HEADERS: ----
            BODY:   username : demo 
                    password : demo@1234
                    password2 : demo@1234
                    email : demo@gmail.com
                    
            OUTPUT: {
                        "response": "Registration Successfully !!!",
                        "username": "smart",
                        "email": "smart@gmail.com",
                        "token": {
                            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTQzMjAwNCwiaWF0IjoxNzI1MzQ1NjA0LCJqdGkiOiJjYzZmYzE5YzQ3MjI0ZjVmOTkyOTE4Yzg3YmRmMjcyMiIsInVzZXJfaWQiOjN9.Jei7oXdyA4CoHczDeQ_B-syrLMdHNKuDgUKgnNIOsBc",
                            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MzQ1OTA0LCJpYXQiOjE3MjUzNDU2MDQsImp0aSI6ImFkYjExODVkY2M2MDRiYjliZmM2MDNkYTVkZjEwNDU0IiwidXNlcl9pZCI6M30.XGBQSTaFZnI4ffqkvEQi8tSS295uz0il1Rjbm1rtpEc"
                        }
                    }


11.Login 
    URL:     http://127.0.0.1:8000/userprofiles/api/token/
    METHOD:  POST
    HEADERS: --
    BODY:   Form Data
             username : smart
             password : smart@123
    OUTPUT: {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTQyODg3OCwiaWF0IjoxNzI1MzQyNDc4LCJqdGkiOiJkZWIxOWFkOGQ5M2U0ZDExYjVhYzczYmY2N2FjNzQzNCIsInVzZXJfaWQiOjF9.FtXK7Xhd5als4fTgwzscHxmhNUaVAnso0ndut2uIzq8",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MzQyNzc4LCJpYXQiOjE3MjUzNDI0NzgsImp0aSI6ImM2ODg3M2FjNjk1NTQwYWNhNDQ5YzgwOGQ2YzU4ZjM0IiwidXNlcl9pZCI6MX0.pzJTb3PUG8tJ2gS4SpUbksJOsKkuJ5S8bxKgiyhQ6_c"
            }
