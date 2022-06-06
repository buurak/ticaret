from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(UserSerializer, self).create(validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {"no_active_account": "Username or password is incorrect."}
