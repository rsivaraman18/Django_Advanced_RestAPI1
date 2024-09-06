from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('login/',      obtain_auth_token , name='login'), ## Token Generation
    path('register/',   views.registration_view), ## On Registering Automatic Token
    path('logout/',     views.logout_view),       ## Delete Token  
    
]
