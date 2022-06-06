from rest_framework import serializers

from product.serializers import ProductDetailSerializer
from .models import Basket, BasketItem


class BasketItemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = BasketItem
        fields = "__all__"

    def get_product(self, obj):
        return ProductDetailSerializer(obj.product).data


class BasketSerializer(serializers.ModelSerializer):
    basket_items = serializers.SerializerMethodField()
    user = serializers.CharField(source="user.full_name")

    class Meta:
        model = Basket
        fields = ["id", "user", "basket_items", "date_ordered", "complete"]

    def get_basket_items(self, obj):
        return BasketItemSerializer(obj.basket_items.all(), many=True).data


class AddItemToBasketSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.FloatField()
