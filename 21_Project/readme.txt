Learn -> 42 to 37 Django Rest Frame Work
This Automatic Token on Login and new urls creations.

1.Create a new Application.
    python manage.py startapp UserProfilesApp

2.Register in setting INSTALLED_APPS.

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Movieapp',
        'UserProfilesApp'
        'rest_framework',
        'rest_framework.authtoken' ,
    ]

3. Project Urls.py
    from django.contrib import admin
    from django.urls import path,include


    urlpatterns = [
        path('admin/',           admin.site.urls),
        path('movieapi/',        include('Movieapp.urls')),
        path('userprofiles/',    include('UserProfilesApp.urls')),
        
    ]

4. Application urls

    from django.urls import path
    from rest_framework.authtoken.views import obtain_auth_token

    urlpatterns = [
        path('login/', obtain_auth_token , name='login'),
        
    ]

5. Create superuser siva
    python manage.py createsuperuser


6. Now go to Postman Application
    TO GET TOKENS FOR USER.
    Urls :   http://127.0.0.1:8000/userprofiles/login/
    Method : POST
    Headers : - 
    Body: Form data username siva  (username,password is keyword in django use it)
                    password siva
    Result :
            New Token will generate for new user siva,token remains same until deleted.
            {
                "token": "e86e575aceb72b8b119b17982939d42f79eadacf"
            }

7.You can genearte token for another user also.
    Repeat step 5 & 6.
    Now new username : demo
            password : Demo@1234
            token : 81a5584abab17dbf8e7c4b94b7a3f8ae6268f90f


8.Write Your Own Url for Review Creation ,Update,etc in MovieApp Application.
    View Codes given in MovieApp


9. Now Using the below URLS and Method You should able to do all the given API call.



    URLS & METHODS
    1.Create a new review
        Urls    : http://127.0.0.1:8000/movieapi/watch/1/review_create/
        Method  : POST
        Headers : Authorization : Token 81a5584abab17dbf8e7c4b94b7a3f8ae6268f90f
        Body    :   {
                        "rating": 5,
                        "description": "Good Movie",
                        "active": true
                    }
        Output  :   {
                        "id": 4,
                        "reviewer_name": "demo",
                        "rating": 5,
                        "description": "Good Movie",
                        "active": true,
                        "created": "2024-08-20T05:56:53.410870Z",
                        "update": "2024-08-20T05:56:53.410870Z"
                }

    2.Show All Reviews
        Urls    : http://127.0.0.1:8000/movieapi/watch/show_reviews/     
        Methods : GET
        Headers : Authorization : Token 81a5584abab17dbf8e7c4b94b7a3f8ae6268f90f
        Body    :   ----
        Output  :   [
                        {
                            "id": 1,
                            "reviewer_name": "siva",
                            "rating": 5,
                            "description": "Good Movie",
                            "active": true,
                            "created": "2024-08-19T11:58:25.168032Z",
                            "update": "2024-08-19T11:58:25.168032Z"
                        },
                        {
                            "id": 2,
                            "reviewer_name": "siva",
                            "rating": 3,
                            "description": "Excellent",
                            "active": true,
                            "created": "2024-08-19T11:58:40.293411Z",
                            "update": "2024-08-19T11:59:05.263083Z"
                        },   
                    ]


    3.Show Reviews in Detail by Id
        Urls    : http://127.0.0.1:8000/movieapi/watch/2/review_detail/     
        Methods : GET
        Headers : ----
        Body    :   ----
        Output  :  
                {
                    "id": 2,
                    "reviewer_name": "siva",
                    "rating": 3,
                    "description": "Excellent",
                    "active": true,
                    "created": "2024-08-19T11:58:40.293411Z",
                    "update": "2024-08-19T11:59:05.263083Z"
                } 
    
    
    4.Review Update by Id
        Urls    : http://127.0.0.1:8000/movieapi/watch/2/review_update/
        Methods : PUT   
        Headers : Authorization : Token 81a5584abab17dbf8e7c4b94b7a3f8ae6268f90f
        Body    :   {
                        "rating": 1,
                        "description": "Fair",
                        "active": true
                    }
        Output  : {
                    "id": 3,
                    "reviewer_name": "demo",
                    "rating": 3,
                    "description": "Average",
                    "active": true,
                    "created": "2024-08-19T12:00:28.098732Z",
                    "update": "2024-08-20T06:03:20.483809Z"
                }



10.Lets Register New User,with automatic token Creation Full Codes.
    10A.UserProfilesApp--> Serializers.py
    
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
    
    
    10B.UserProfilesApp--> Urls.py
        from django.urls import path
        from rest_framework.authtoken.views import obtain_auth_token
        from . import views

        urlpatterns = [
            path('login/',    obtain_auth_token , name='login'),
            path('register/', views.registration_view),    
        ]

    10C.UserProfilesApp--> Views.py
        from rest_framework.decorators import api_view
        from rest_framework.response import Response
        from rest_framework.authtoken.models import Token
        from UserProfilesApp.serializers import *
        from UserProfilesApp.models import *

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
                    token = Token.objects.get(user=account).key
                    print('Token : ',token)
                    data['token'] = token    
                else:
                    data = serializer.errors
                return Response(data)
    
    10D.UserProfilesApp--> Models.py
        from django.conf import settings
        from django.db.models.signals import post_save
        from django.dispatch import receiver
        from rest_framework.authtoken.models import Token

        @receiver(post_save,sender=settings.AUTH_USER_MODEL)
        def create_auth_token(sender,instance=None,created=False,**kwargs):
            if created:
                Token.objects.create(user=instance)

11.Create New user with automatic token Generation

        Urls    : http://127.0.0.1:8000/userprofiles/register/
        Methods : POST   
        Headers : ----
        Body    : formdata 
                    username : example3
                    email :example3@gmail.com
                    password : example@1234
                    password1 : example@1234

        Output  :{
                    "response": "Registration Successfully !!!",
                    "username": "example3",
                    "email": "example3@gmail.com",
                    "token": "7a055447f29881ca59d13875b1caae72f22a324b"
                }



12. Now on Logout token should be deleted for the user

12A.Urls.py
    from django.urls import path
    from rest_framework.authtoken.views import obtain_auth_token
    from . import views

    urlpatterns = [
        path('login/',      obtain_auth_token , name='login'), ## Token Generation
        path('register/',   views.registration_view), ## On Registering Automatic Token
        path('logout/',     views.logout_view),       ## Delete Token  
        
    ]


12B.Views.py
    @api_view(['POST',])
    def logout_view(request):

        if request.method == 'POST':
            request.user.auth_token.delete()
            return Response(status=status.HTTP_200_OK) 

13. Try Logout in Postman

    Urls    : http://127.0.0.1:8000/userprofiles/logout/
    Methods : POST   
    Headers : Authorization Token d80bb98da899aeea453c53a635ce89cd55cb7ca4
    Body    : formdata 
                username : example3
                password : example@1234
                

    Output  : {
                "message": "example1Token Deleted"
            }
            Status 200



14.Final   Summary.
    14A.You can create new user and and automatic token Generation.
        Urls    : http://127.0.0.1:8000/userprofiles/register/
        Methods : POST   
        Headers : ----
        Body    : --> formdata 
                        username : example3
                        email :example3@gmail.com
                        password : example@1234
                        password1 : example@1234

                
        Output  : {
                    "response": "Registration Successfully !!!",
                    "username": "example1",
                    "email": "example1@gmail.com",
                    "token": "83ed4689410f99fda96f776e4b94f369e2cc7315"
                    } 

    14B.You can Delete Token of Particular User.
        Urls    : http://127.0.0.1:8000/userprofiles/logout/
        Methods : POST   
        Headers : Authorization Token 2bda1b74ca931e0d5f4d0e64c614e4c50293ff9f
        Body    : --> formdata 
                        username : example3
                        password : example@1234
                        
                
        Output  : {
                    "message": "example1Token Deleted"
                    }
    14C.You can Generate a new token of already registered User.
        Urls    : http://127.0.0.1:8000/userprofiles/login/
        Methods : POST   
        Headers : ----
        Body    : --> formdata 
                        username : example3
                        password : example@1234
                    
                
        Output  : {
                    "token": "2bda1b74ca931e0d5f4d0e64c614e4c50293ff9f"
                } 






















        



        






    






















