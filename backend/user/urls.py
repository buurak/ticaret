from django.urls import path

from .views import CreateUserAPIView, LoginAPIView

urlpatterns = [
    path('api/register/', CreateUserAPIView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='token_obtain_pair'),
]
