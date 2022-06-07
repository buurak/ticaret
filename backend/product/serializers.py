from rest_framework.serializers import ModelSerializer

from product.models import Product, ProductCategory


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "stock", "photo", "price"]


class ProductDetailSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
