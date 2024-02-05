

from urllib import request
from django.shortcuts import render
from product.models import Product , Category
# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request,'core/frontpage.html',{'products': products})


def shop(request):
    products = Product.objects.all()
    catagories = Category.objects.all()

    context = {
        'catagories' : catagories,
        'products' : products
    }
    return render(request,'core/shop.html',{'products': products})
    
