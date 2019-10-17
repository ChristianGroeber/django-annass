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
