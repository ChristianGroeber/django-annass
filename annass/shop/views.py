from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Product, ShoppingCart, CartItem


def index(request):
    products = Product.objects.filter(is_active=True)
    shoppingCartId = request.COOKIES.get('shoppingCartId')
    if not shoppingCartId:
        shoppingCart = ShoppingCart()
        shoppingCart.save()
        shoppingCartId = shoppingCart.id
    return render(request, 'shop/index.html', {"products": products, "shoppingCartId": shoppingCartId})


def update_shopping_cart(request):
    shoppingCartId = request.POST.get('shoppingCart')
    cart = ShoppingCart.objects.get(pk=shoppingCartId)
    price = cart.calculate_price()
    return JsonResponse({'price': price})


def add_item_to_cart(request):
    cart = ShoppingCart.objects.get(request.POST.get('shoppingCart'))
    item = Product.objects.get(request.POST.get('product'))

    cartItem = CartItem()
    cartItem.product = item
    cartItem.cart = cart

    return JsonResponse({})
