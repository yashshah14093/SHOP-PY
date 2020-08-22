from django.shortcuts import render
from products.models import Product
# Create your views here.

def prod_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

