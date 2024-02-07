

from urllib import request
from django.shortcuts import render
from product.models import Product , Category
# Create your views here.

def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request,'core/frontpage.html',{'products': products})


def shop(request):
    catagories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category','')
    context = {
        'catagories' : catagories,
        'products' : products,
        'active_category' : active_category
    }
    return render(request,'core/shop.html',context)
    
