from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('update-shopping-cart/', views.update_shopping_cart, name='update_shopping_cart'),
    path('add-item-to-cart/', views.add_item_to_cart, name='add_item_to_cart'),
]
