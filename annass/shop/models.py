from django.db import models

# Create your models here.
from django.db.models import ImageField


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    price = models.IntegerField()
    image = ImageField(upload_to="shop/product-images", blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Aktiv?')

    def __str__(self):
        return self.name

    def to_array(self):
        ret = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
        }
        if self.image:
            ret['image'] = self.image.url
        else:
            ret['image'] = None

        return ret


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255, verbose_name="Beschreibung", blank=True)
    products = models.ManyToManyField(Product, blank=True)
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
