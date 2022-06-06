from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, CustomTokenObtainPairSerializer


class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
