from django.urls import path

from .views import CheckOutView

urlpatterns = [
    path('api/order/', CheckOutView.as_view(), name='order'),
]
