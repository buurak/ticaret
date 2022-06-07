from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product, ProductCategory
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductCategorySerializer


class ProductListView(APIView):
    def get(self, request):
        qs = Product.objects.all()

        if category_id := request.query_params.getlist("category"):
            categories = [int(x) for x in category_id[0].split(",")]
            qs = qs.filter(categories__in=categories)

        serialized_data = ProductListSerializer(qs, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    def get(self, request, _id):
        obj = get_object_or_404(Product, id=_id)
        serialized_data = ProductDetailSerializer(obj).data

        return Response(serialized_data, status=status.HTTP_200_OK)


class ProductCategoryListView(APIView):
    def get(self, request):
        qs = ProductCategory.objects.all()
        serialized_data = ProductCategorySerializer(qs, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)
