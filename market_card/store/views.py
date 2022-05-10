from django.shortcuts import render
from .models import Product


def store(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)

def cart(request, pk): 
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'store/cart.html', context)

def crear_product(request):
    return render(request,'crear_product.html')