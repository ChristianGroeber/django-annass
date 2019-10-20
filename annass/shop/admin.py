from django.contrib import admin
from .models import Product, ShoppingCart, ProductCategory

admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(ProductCategory)
