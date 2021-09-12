from django.shortcuts import render,redirect
from .models import Product

# Create your views here.

def prod_delete(request,id):
    prod = Product.objects.get(pk=id)
    prod.delete()
    return redirect('')
