from django.contrib import admin
from .models import Product, ShoppingCart, ProductCategory, CartItem

admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(ProductCategory)
admin.site.register(CartItem)
