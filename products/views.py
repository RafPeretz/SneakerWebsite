from django.shortcuts import render
from .models import Sneakers
from django.shortcuts import get_object_or_404


def index(request):
    sneakers = Sneakers.objects.all()
    context = {
        'sneakers': sneakers
    }
    return render(request, 'products/products.html', context)


def product(request, product_id):
    sneakers = get_object_or_404(Sneakers, pk=product_id)
    context = {
        'sneakers': sneakers
    }
    return render(request, 'products/product.html', context)


def search(request):
    return render(request, 'products/search.html')
# Create your views here.
