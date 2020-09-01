from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Business, Designer, Product, ProductImage, ProductStock

# Create your views here.
def index(request):
    """The home page for the retail app, Find and Seek"""

    """Show all products, businesses, and designers."""
    products = Product.objects.order_by("designer")
    businesses = Business.objects.order_by("name")
    designers = Designer.objects.order_by("name")
    business_name = businesses[0].name

    for product in products:
        product.images = ProductImage.objects.filter(product=product.pk)
        product.stock = ProductStock.objects.filter(product=product.pk)

    try:
        context = {
            "products": products,
            "businesses": businesses,
            "designers": designers,
            "name": business_name,
        }

    except businesses.DoesNotExist and designers.DoesNotExist:
        raise Http404("Data does not exist")

    return render(request, "retail_app/index.html", context)
