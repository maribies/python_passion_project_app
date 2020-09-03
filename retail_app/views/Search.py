from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from retail_app.models import (
    Business,
    Designer,
    Product,
    ProductImage,
    ProductStock,
    SearchProductKeywords,
)


def search(request):
    """The search page for the retail app, Find and Seek"""

    """Show search results for all products, businesses, and designers."""
    try:
        query = request.GET.get("userSearchInput")
        products = Product.objects.filter(Q(designer__contains=query))
        businesses = Business.objects.order_by("name")
        designers = Designer.objects.order_by("name")

        for product in products:
            product.images = product.productimage_set.all()[0:2]
            product.stock = product.productstock_set.all()
            product.keywords = product.searchproductkeywords_set.all()

        context = {
            "products": products,
            "businesses": businesses,
            "designers": designers,
        }

    except IndexError or AttributeError or ValueError:
        raise Http404("Something went wrong!")

    return render(request, "retail_app/searchContent.html", context)
