from django.views.generic import ListView
from django.shortcuts import render
from products.models import Product


class HomePageView(ListView):
    model = Product
    template_name = 'index.html'
