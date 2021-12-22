from django.shortcuts import render
from django.http import HttpResponse
from products.models import Sneakers
from size.models import Size
from category.models import Category
from company.models import Company


# Create your views here.
def index(request):
    sneakers = Sneakers.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'sneakers': sneakers
    }
    return render(request, '../templates/home.html', context)


def about(request):
    company = Company.objects.all()
    context = {
        'company': company
    }
    return render(request, '../templates/about.html', context)
