from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from basket.models import Basket
from basket.serializers import BasketSerializer
from djangoProject.views import BaseAPIView


class CheckOutView(BaseAPIView):

    def get(self, request):
        qs = Basket.objects.filter(complete=True, user_id=request.query_params["user_id"]).order_by("-date_ordered")
        serializer = BasketSerializer(qs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        basket = get_object_or_404(Basket.actives, user=request.data["user_id"])

        if not basket.get_basket_price:
            Response({"message": "Basket is empty!"}, status=status.HTTP_400_BAD_REQUEST)

        basket.complete = True
        basket.save()

        return Response(BasketSerializer(basket).data, status=status.HTTP_201_CREATED)
