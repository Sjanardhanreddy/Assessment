from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def product_details(request):
    product = product.objects.get()
    image = image.objects.filter(product_id= id)
    context={
        'product':product,
        'images': image
    }
    return render(request, 'product_app.html', context)