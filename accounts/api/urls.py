from django.urls import path
from accounts.api.views import (
    registration_view,
)

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt import views as jwt_views

app_name = 'accounts'

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('sessions/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('sessions/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh')


]
