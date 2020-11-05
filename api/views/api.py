from django.http import JsonResponse
from api.serializers import ProductSerializer
from retail_app.models import Product
import json
from django.core.paginator import Paginator


def get_data(request):
    """The API for Find and Seek products resposnse"""

    try:
        if request is None:
            raise Exception("Houston, we have a problem.")

        # search = request.GET.get("search")
        page = request.GET.get("page")
        per_page = request.GET.get("per_page")

        products = Product.objects.fully_loaded_objects()
        products_for_serialization = products

        if page is not None and per_page is not None:
            paginator = Paginator(products, per_page)
            products_for_serialization = paginator.get_page(page)

            if len(products) / int(per_page) < int(page) or int(page) == 0:
                products_for_serialization = []

        serializedProducts = [
            ProductSerializer(product).to_json()
            for product in products_for_serialization
        ]

        products_data = {"products": serializedProducts}

        return JsonResponse(products_data)

    # If error, send error message.
    except Exception as e:
        print("error!", e)
