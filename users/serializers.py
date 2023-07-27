from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        User = get_user_model()
        model = User
        fields = ('id', 'password', 'email')

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create_user(**validated_data)
        return user

