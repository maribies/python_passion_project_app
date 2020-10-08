from django.shortcuts import render
from django.http import Http404

from retail_app.models import Designer, Product


def filters(request):
    """The home page for the retail app, Find and Seek"""

    """Show filtered products by designer."""
    try:
        chosen_filter = request.GET.get("designer_filter")

        products = (
            Product.objects.filter(designer=chosen_filter)
            .select_related("product_price")
            .prefetch_related(
                "productimage_set",
                "productstock_set",
                "productstock_set__color",
            )
        )

        designers = Designer.objects.order_by("name")

        context = {
            "products": products,
            "designers": designers,
            "chosen_filter": chosen_filter,
            "results": len(products),
        }

    except IndexError or AttributeError:
        raise Http404("Something went wrong!")

    return render(request, "retail_app/filter_content.html", context)
