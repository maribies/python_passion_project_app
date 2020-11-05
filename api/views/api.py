from django.http import JsonResponse
from api.serializers import ProductSerializer
from retail_app.models import Product
import json


def get_data(request):
    """The API for Find and Seek products resposnse"""

    try:
        if request is None:
            raise Exception("Houston, we have a problem.")

        search = request.GET.get("search")
        page = request.GET.get("page")
        per_page = request.GET.get("per_page")

        print("options", search, page, per_page)

        products = Product.objects.fully_loaded_objects()
        serializedProducts = [
            ProductSerializer(product).to_json() for product in products
        ]

        products_data = {"products": serializedProducts}

        return JsonResponse(products_data)

    # If error, send error message.
    except Exception as e:
        print("error!", e)
