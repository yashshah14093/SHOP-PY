from django.shortcuts import render
from products.models import Product
from rest_framework.decorators import api_view
from products.serializers import Productserializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(["GET","POST"])

def show_list(request):
    if(request.method == "GET"):
        data = Product.objects.all()
        serializers = Productserializer(data,many=True)
        return Response(serializers.data)
    elif(request.method == "POST"):
        serializers = Productserializer(data = request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


def prod_index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

