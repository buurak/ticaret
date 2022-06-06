from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from basket.models import Basket
from basket.serializers import BasketSerializer


class CheckOutView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        qs = Basket.objects.filter(complete=True).order_by("-date_ordered")
        serializer = BasketSerializer(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        basket = get_object_or_404(Basket.actives, user=request.user)

        if not basket.get_basket_price:
            Response({"message": "Basket is empty!"})

        basket.complete = True
        basket.save()

        return Response(status=status.HTTP_201_CREATED)
