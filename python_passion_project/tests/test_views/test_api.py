from django.test import RequestFactory, TestCase, Client
from api.views import api
from model_bakery import baker
import json
from retail_app.models import (
    Product,
)


class TestApiView(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        self.products = baker.make_recipe("retail_app.products_test", _quantity=20)

    # def test_get_data_all(self):
    #     request = self.factory.get(
    #         "/api/v1/products/",
    #         {"search": "", "page": 1, "per_page": 10},
    #     )

    #     response = api.get_data(request)

    #     content = response.content.decode("utf-8")

    #     # Response content should be all products.

    #     products = json.loads(content)['products']
    #     self.assertEqual(response.status_code, 200)
    #     self.assertNotEqual(content, '{"products": []}')
    #     self.assertEqual(len(products), 10)

    def test_get_data_none(self):
        response = self.c.get("/api/v1/products/", {})

        # This also works.
        # request = self.factory.get("api/v1/products/", {})
        # response = api.get_data(request)

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(content, '{"products": []}')
        self.assertEqual(len(products), 20)

    # def test_get_data_search_designer(self):
    #     request = self.factory.get(
    #         "/api/v1/products/",
    #         {"search": "Chanel", "page": 1, "per_page": 10},
    #     )

    #     response = api.get_data(request)

    #     print("testSearchDesigner", response, response.content)
    #     # Check the response content is for Chanel products only.

    #     self.assertEqual(response.status_code, 200)

    # def test_get_data_search_color(self):
    #     request = self.factory.get(
    #         "/api/v1/products/",
    #         {"search": "black", "page": 1, "per_page": 10},
    #     )

    #     response = api.get_data(request)

    #     print("testSearchColor", response, response.content)
    #     # Check the response content is for black products only.

    #     self.assertEqual(response.status_code, 200)

    # def test_get_data_search_two(self):
    #     request = self.factory.get(
    #         "/api/v1/products/",
    #         {"filter_designer": "", "search": "Chanel black", "page": 1, "per_page": 10},
    #     )

    #     response = api.get_data(request)

    #     print("testSearch2", response, response.content)
    #     # Check the response content is for black Chanel products only.

    #     self.assertEqual(response.status_code, 200)
