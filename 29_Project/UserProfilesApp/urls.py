from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('login/',      obtain_auth_token,        name='UserLogin'), 
    path('register/',   views.registration_view,  name='UserRegister'), 
    path('logout/',     views.logout_view,        name='UserLogout'),
]


"""
On Registering --> Automatic Token Generated
On Login       --> Token is used for access
On Logout      --> Delete the User Token
"""
