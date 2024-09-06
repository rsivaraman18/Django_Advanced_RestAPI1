from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token
from . import views


from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
    


urlpatterns = [
    
    path('register/',   views.registration_view), ## On Registering Automatic Token
    path('logout/',     views.logout_view),       ## Delete Token  

    #### JWT TOKEN AUTHENTICATION
    path('api/token/',         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]
