from django.db import models

from product.models import Product
from .manager import BasketActivesManager


class Basket(models.Model):
    user = models.ForeignKey(to="user.User", on_delete=models.CASCADE, related_name="basket", verbose_name="user")
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    objects = models.Manager()
    actives = BasketActivesManager()

    def __str__(self):
        return self.user.full_name

    @property
    def get_basket_price(self):
        if qs := self.basket_items.all():
            return sum([item.get_total for item in qs])
        return 0


class BasketItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    basket = models.ForeignKey(Basket, on_delete=models.SET_NULL, null=True, related_name="basket_items")
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Basket Item"
        verbose_name_plural = "Basket Items"

    def __str__(self):
        return f"{self.product.title} | ₺{self.product.price * self.quantity}"

    @property
    def get_total(self):
        return self.product.price * self.quantity
