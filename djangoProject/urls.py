from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user.urls")),
    path('', include("product.urls")),
    path('', include("basket.urls")),
    path('', include("order.urls")),
]
