from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator

from retail_app.models import Designer, Product


def index(request):
    """The home page for the retail app, Find and Seek"""

    """Show all purple (featured) products and designers."""
    try:
        products = Product.objects.fully_loaded_objects().filter(
            productstock__color__color__icontains="purple"
        )

        designers = Designer.objects.order_by("name")

        page = request.GET.get("page", 1)
        paginated_products = Paginator(products, 12).get_page(page)

        context = {
            "products": paginated_products,
            "designers": designers,
        }

    except IndexError or AttributeError:
        raise Http404("Something went wrong!")

    return render(request, "retail_app/index.html", context)
