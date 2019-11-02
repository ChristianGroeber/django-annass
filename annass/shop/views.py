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


def checkout(request):
    cart = ShoppingCart.objects.get(pk=request.COOKIES.get('shoppingCartId'))
    return render(request, 'shop/checkout.html', {'products': cart.to_array()})


def update_amount_of_products(request):
    product = CartItem.objects.get(pk=request.POST.get('itemId'))
    if request.POST.get('action') == 'remove':
        product.amount -= 1
    else:
        product.amount += 1
    product.save()
    return JsonResponse({})


def update_shopping_cart(request):
    shoppingCartId = request.POST.get('shoppingCart')
    cart = ShoppingCart.objects.get(pk=shoppingCartId)
    price = cart.calculate_price()
    return JsonResponse({'price': price})


def add_item_to_cart(request):
    if not request.POST.get('productId') and not request.POST.get('cartItemId'):
        return JsonResponse({})
    cart = ShoppingCart.objects.get(id=request.COOKIES.get('shoppingCartId'))

    print(request.POST)

    cart_item = None
    item = None
    if request.POST.get('productId'):
        item = Product.objects.get(id=request.POST.get('productId'))
    else:
        cart_item = CartItem.objects.get(pk=request.POST.get('cartItemId'))

    if item:
        for product in cart.products.all():
            if item == product.product:
                cart_item = product

    if not cart_item:
        cart_item = CartItem()
        cart_item.product = item
        cart_item.amount = 0
        cart_item.save()
        cart.products.add(cart_item)

    cart_item.amount += 1
    cart_item.save()

    cart.save()

    return JsonResponse({'productId': request.POST.get('cartItemId'), 'price': cart.calculate_price(), 'amount': cart_item.amount, 'productPrice': cart_item.product.price * cart_item.amount})


def remove_item_from_cart(request):
    if not request.POST.get('productId'):
        return JsonResponse({})
    item = CartItem.objects.get(pk=request.POST.get('productId'))
    item.amount -= 1
    item.save()

    cart = None
    for shopping_cart in ShoppingCart.objects.all():
        if item in shopping_cart.products.all():
            cart = shopping_cart
            break

    return JsonResponse({'productId': request.POST.get('productId'), 'price': cart.calculate_price(), 'amount': item.amount, 'productPrice': item.product.price * item.amount})


def load_product_category(request):
    category = ProductCategory.objects.get(name=request.POST.get('categoryName'))
    products = category.products.filter(is_active=True)
    return JsonResponse({'products': queryset_to_array(products), 'categoryName': request.POST.get('categoryName')})


def queryset_to_array(queryset):
    ret = []
    for item in queryset:
        ret.append(item.to_array())
    return ret
