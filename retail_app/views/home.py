from django.shortcuts import render
from django.http import Http404

from retail_app.models import Business, Designer, Product


def index(request):
    """The home page for the retail app, Find and Seek"""

    """Show all products, businesses, and designers."""
    try:
        products = (
            Product.objects.order_by("designer")
            .select_related("product_price")
            .prefetch_related("productimage_set")
            .prefetch_related("productstock_set__color")
        )

        designers = Designer.objects.order_by("name")

        context = {
            "products": products,
            "designers": designers,
        }

    except IndexError or AttributeError:
        raise Http404("Something went wrong!")

    return render(request, "retail_app/index.html", context)
