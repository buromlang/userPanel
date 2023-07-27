
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
