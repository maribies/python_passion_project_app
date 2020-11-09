from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re

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

        query_text = re.sub(r"\?(.*)", " ", query).strip()
        query_page = re.findall(r"\d+", query)
        if len(query_page) == 0:
            page = 1
        else:
            page = query_page.pop(0)

        keywords = (
            SearchProductKeywords.objects.filter(keywords__icontains=query_text)
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

        paginated_products = Paginator(products, 24)

        try:
            products = paginated_products.page(page)
        except PageNotAnInteger:
            products = paginated_products.page(1)
        except EmptyPage:
            products = paginated_products.page(paginated_products.num_pages)

        context = {
            "products": products,
            "designers": designers,
            "results": len(keywords),
            "query_text": query_text,
            "query": query,
        }

    except IndexError or AttributeError or ValueError:
        raise Http404("Something went wrong!")

    except Exception:
        # TODO: Add model manager for context so it's not an empty page.
        return render(request, "retail_app/index.html")

    return render(request, "retail_app/search_content.html", context)
