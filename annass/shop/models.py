from django.db import models

# Create your models here.
from django.db.models import ImageField


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=255, blank=False)
    image = ImageField(upload_to="shop/product-images", blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Aktiv?')

    def __str__(self):
        return self.name


class ShoppingCart(models.Model):
    products = models.ManyToManyField(Product)

    def __str__(self):
        return "Einkaufswagen" + str(self.id)

    def calculate_price(self):
        price = 0
        for product in self.products.all():
            price += product.price
        return price


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
