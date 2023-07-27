from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from rest_framework.authtoken import views


routers = routers.DefaultRouter()
routers.register('users', UserViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    path('login/', views.obtain_auth_token),
]