from django.urls import path

from .views import BasketProductAPIView

urlpatterns = [
    path('api/basket/', BasketProductAPIView.as_view(), name='basket'),
]
