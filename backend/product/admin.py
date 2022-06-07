from django.contrib import admin

from .models import Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)
