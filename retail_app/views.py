from django.shortcuts import render
from django.http import Http404

from .models import Business, Designer, Product, ProductImage, ProductStock


def index(request):
    """The home page for the retail app, Find and Seek"""

    """Show all products, businesses, and designers."""
    try:
        products = Product.objects.order_by("designer")
        businesses = Business.objects.order_by("name")
        designers = Designer.objects.order_by("name")
        business_name = businesses[0].name

        for product in products:
            product.images = product.productimage_set.all()[0:2]
            product.stock = product.productstock_set.all()

        context = {
            "products": products,
            "businesses": businesses,
            "designers": designers,
            "name": business_name,
        }

    except IndexError or AttributeError:
        raise Http404("Something went wrong!")

    return render(request, "retail_app/index.html", context)
