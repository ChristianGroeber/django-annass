from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'shop/index.html', {"products": products})
