from django.db import models


class SizeChoices(models.TextChoices):
    XS = "X Small"
    S = "Small"
    M = "Medium"
    L = "Large"
    XL = "X Large"
    XXL = "XX Large"


class ColorChoices(models.TextChoices):
    RED = "red"
    YELLOW = "yellow"
    BLUE = "blue"
    PURPLE = "purple"
    GREEN = "green"
    PINK = "pink"


class ProductCategory(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(choices=ColorChoices.choices, max_length=255)
    stock = models.PositiveIntegerField()
    price = models.FloatField(null=False, blank=False)
    size = models.CharField(choices=SizeChoices.choices, max_length=255)
    photo = models.ImageField(max_length=255, null=True, blank=False)
    categories = models.ManyToManyField(
        to=ProductCategory, related_name="products", verbose_name="category"
    )

    def __str__(self):
        return self.title
