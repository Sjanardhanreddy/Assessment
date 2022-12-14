from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Product, Image

# Create your views here.
def product(request):
    product = product.objects.get()
    image = image.objects.filter(product_id= id)
    context={
        'product':product,
        'images': image
    }
    return render(request, 'product.html', context)
