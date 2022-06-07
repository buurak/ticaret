from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoProject.views import BaseAPIView
from product.models import Product
from .models import Basket, BasketItem
from .serializers import BasketSerializer, BasketItemSerializer, AddItemToBasketSerializer


class BasketProductAPIView(BaseAPIView):
    def get(self, request):
        qs, _ = Basket.actives.get_or_create(user_id=self.request.query_params["user_id"])

        return Response(BasketSerializer(qs).data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddItemToBasketSerializer(data=request.data)
        serializer.is_valid()

        basket, _ = Basket.actives.get_or_create(user_id=self.request.data["user_id"])
        product = get_object_or_404(Product, id=serializer.validated_data["id"])
        basket_item, created = BasketItem.objects.get_or_create(
            basket=basket, product=product, defaults={"quantity": serializer.validated_data["quantity"]}
        )
        basket_item.quantity += serializer.validated_data["quantity"]
        if product.stock < basket_item.quantity:
            return Response({"message": "Not enough stock on this product"}, status=status.HTTP_400_BAD_REQUEST)

        basket_item.save()

        return Response(BasketItemSerializer(basket_item).data, status=status.HTTP_201_CREATED)

    def put(self, request):
        serializer = AddItemToBasketSerializer(data=request.data)
        serializer.is_valid()

        if serializer.validated_data["quantity"] == 0:
            BasketItem.objects.filter(
                basket__user_id=self.request.data["user_id"], id=serializer.validated_data["id"]
            ).delete()
        else:
            BasketItem.objects.filter(
                basket__user_id=self.request.data["user_id"], id=serializer.validated_data["id"]
            ).update(
                quantity=serializer.validated_data["quantity"]
            )

        return Response({"status": True}, status=status.HTTP_205_RESET_CONTENT)

    def delete(self, request):
        Basket.actives.filter(user_id=self.request.data["user_id"]).delete()

        return Response(status=status.HTTP_205_RESET_CONTENT)
