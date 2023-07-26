from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False)
    def login(self, request):
        queryset = get_object_or_404(self.queryset, email=request.data['email'])
        if queryset.password == request.data['password']:
            token, _ = Token.objects.get_or_create(queryset)
            return Response(token.key, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)


