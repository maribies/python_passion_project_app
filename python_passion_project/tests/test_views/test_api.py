from django.test import TestCase, Client
from api.views import api
from model_bakery import baker
import json
from retail_app.models import (
    Product,
)


class TestApiView(TestCase):
    def setUp(self):
        self.client = Client()
        self.products = baker.make_recipe("retail_app.products_test", _quantity=20)

    def test_get_data_none(self):
        response = self.client.get("/api/v1/products/", {})

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(content, '{"products": []}')
        self.assertEqual(len(products), 20)
