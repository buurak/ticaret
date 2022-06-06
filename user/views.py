from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class CreateUserAPIView(APIView):
    def post(self, request):
        user, created = User.objects.get_or_create(
            email=request.data["email"],
            defaults=dict(first_name=request.data["first_name"], last_name=request.data["last_name"])
        )
        if created:
            user.set_password(request.data["password"])
            user.save()

            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response({"message": "There is already an account"}, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.get(email=request.data["email"])
        if user.check_password(request.data["password"]):
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        return Response({"status": False}, status=status.HTTP_200_OK)
