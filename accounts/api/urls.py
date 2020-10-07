from django.urls import path
from accounts.api.views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('sessions/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('sessions/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')

]
