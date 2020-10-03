from django.contrib import admin
from django.urls import path, include
from school.views import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
