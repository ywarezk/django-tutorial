from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, min_length=5)
    password = serializers.CharField(required=True, min_length=8, max_length=30)
    username = serializers.CharField(required=True, min_length=3, max_length=30)
    def create(self, validated_data):
        if len(User.objects.filter(email=validated_data["email"])) == 0:
            user = User()
            user.email = validated_data["email"]
            user.password = validated_data["password"]
            user.username = validated_data["username"]
            user.save()