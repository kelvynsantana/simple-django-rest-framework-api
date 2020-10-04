from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.api import urls as accounts_urls

router = routers.DefaultRouter()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/accounts/', include(accounts_urls, 'accounts_api'))
]
