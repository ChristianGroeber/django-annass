from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Product, ShoppingCart, CartItem, ProductCategory


def index(request):
    products = Product.objects.filter(is_active=True)
    shoppingCartId = request.COOKIES.get('shoppingCartId')
    productCategories = ProductCategory.objects.filter(is_active=True)
    if not shoppingCartId:
        shoppingCart = ShoppingCart()
        shoppingCart.save()
        shoppingCartId = shoppingCart.id
    return render(request, 'shop/index.html', {"products": products, "productCategories": productCategories, "shoppingCartId": shoppingCartId})


def update_shopping_cart(request):
    shoppingCartId = request.POST.get('shoppingCart')
    cart = ShoppingCart.objects.get(pk=shoppingCartId)
    price = cart.calculate_price()
    return JsonResponse({'price': price})


def add_item_to_cart(request):
    if not request.POST.get('productId'):
        return JsonResponse({})

    cart = ShoppingCart.objects.get(request.POST.get('shoppingCart'))
    item = Product.objects.get(request.POST.get('productId'))

    cartItem = CartItem()
    cartItem.product = item
    cartItem.cart = cart

    cartItem.save()

    return JsonResponse({})


def load_product_category(request):
    category = ProductCategory.objects.get(name=request.POST.get('categoryName'))
    products = category.products.filter(is_active=True)
    return JsonResponse({'products': queryset_to_array(products), 'categoryName': request.POST.get('categoryName')})


def queryset_to_array(queryset):
    ret = []
    for item in queryset:
        ret.append(item.to_array())
    return ret
