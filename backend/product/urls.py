from django.urls import path


from .views import ProductListView, ProductDetailView, ProductCategoryListView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='register'),
    path('api/product/<str:_id>', ProductDetailView.as_view(), name='product_detail'),
    path('api/product-categories/', ProductCategoryListView.as_view(), name='product_category_list'),
]
