from django.http import JsonResponse
from api.serializers import ProductSerializer
from retail_app.models import Product, SearchProductKeywords
import json
from django.core.paginator import Paginator
import math


def get_data(request):
    """The API for Find and Seek products resposnse"""

    try:
        if request is None:
            raise Exception("Houston, we have a problem.")

        page = request.GET.get("page", 1)
        per_page = request.GET.get("per_page", 12)

        search = request.GET.get("search")

        if search is not None:
            keywords = (
                SearchProductKeywords.objects.filter(keywords__icontains=search)
                .select_related("product")
                .select_related("product__product_price")
                .prefetch_related(
                    "product__productimage_set",
                    "product__productstock_set",
                    "product__productstock_set__color",
                )
            )
            products = [keyword.product for keyword in keywords]

        else:
            products = Product.objects.fully_loaded_objects()

        paginator = Paginator(products, per_page)
        products_for_serialization = paginator.get_page(page)

        num_of_pages = paginator.num_pages

        if int(page) > num_of_pages or int(page) == 0:
            products_for_serialization = []

        serialized_products = [
            ProductSerializer(product).to_json()
            for product in products_for_serialization
        ]

        products_data = {"products": serialized_products}

        return JsonResponse(products_data)

    # If error, send error message.
    except ValueError:
        return JsonResponse({"products": []})
    except Exception as e:
        print("error!", e)
