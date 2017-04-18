from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, min_length=5)
    password = serializers.CharField(required=True, min_length=8, max_length=30)

    def create(self, validated_data):
        """

        :param validated_data: 
        :return: 
        """

        user = get_object_or_404(User, email=validated_data['email'])
        if not user.check_password(validated_data['password']):
            raise AuthenticationFailed()
        return user
