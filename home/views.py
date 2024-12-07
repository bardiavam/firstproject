from itertools import product

from django.shortcuts import render

from home.models import Category, Products


# Create your views here.

def home(request):
    cat = Category.objects.all()
    return render(request , 'home/home.html',context={'cat':cat})

def products(request):
    cat = Products.objects.all()
    return render(request, 'home/product.html',context={'cat':cat})

def detail(request,id):
    product = Products.objects.get(id=id)
    return render(request, 'home/detail.html',context={'product':product})