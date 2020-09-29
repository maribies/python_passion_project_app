from django.shortcuts import render
from django.http import Http404

from retail_app.models import Designer, Product


def index(request):
    """The home page for the retail app, Find and Seek"""

    """Show all products and designers."""
    try:
        products = Product.products_fully_loaded()

        designers = Designer.objects.order_by("name")

        context = {
            "products": products,
            "designers": designers,
        }

    except IndexError or AttributeError:
        raise Http404("Something went wrong!")

    return render(request, "retail_app/index.html", context)
