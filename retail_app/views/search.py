from django.shortcuts import render
from django.http import Http404

from retail_app.models import (
    Designer,
    SearchProductKeywords,
)


def search(request):
    """The search page for the retail app, Find and Seek"""

    """Show search results for all products and designers."""
    try:
        query = request.GET.get("search")

        if query is None:
            raise Exception("Query can't be None.")

        keywords = (
            SearchProductKeywords.objects.filter(keywords__icontains=query)
            .select_related("product")
            .select_related("product__product_price")
            .prefetch_related(
                "product__productimage_set",
                "product__productstock_set",
                "product__productstock_set__color",
            )
        )
        products = [keyword.product for keyword in keywords]
        designers = Designer.objects.order_by("name")

        context = {
            "products": products,
            "designers": designers,
            "results": len(keywords),
            "query": query,
        }

    except IndexError or AttributeError or ValueError:
        raise Http404("Something went wrong!")

    except Exception:
        # TODO: Add model manager for context so it's not an empty page.
        return render(request, "retail_app/index.html")

    return render(request, "retail_app/search_content.html", context)
