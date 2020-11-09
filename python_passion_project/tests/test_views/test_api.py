from django.test import TestCase, Client
from model_bakery import baker
import json


class TestApiView(TestCase):
    def setUp(self):
        self.client = Client()
        self.products = baker.make_recipe("retail_app.products_test", _quantity=21)

    def test_get_data_none(self):
        response = self.client.get("/api/v1/products/", {})

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(content, '{"products": []}')
        self.assertEqual(len(products), 12)

    def test_get_data_pagination_one(self):
        response = self.client.get(
            "/api/v1/products/",
            {"page": 1, "per_page": 10},
        )

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(content, '{"products": []}')
        self.assertEqual(len(products), 10)

    def test_get_data_pagination_word(self):
        response = self.client.get(
            "/api/v1/products/",
            {"page": "one", "per_page": 10},
        )

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, '{"products": []}')
        self.assertEqual(len(products), 0)

    def test_get_data_pagination_at_end(self):
        response = self.client.get(
            "/api/v1/products/",
            {"page": 3, "per_page": 10},
        )

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]
        first_product_name = json.loads(products[0])["name"]

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(content, '{"products": []}')
        self.assertEqual(len(products), 1)
        self.assertEqual(first_product_name, "Test Product21")

    def test_get_data_pagination_beyond_end(self):
        response = self.client.get(
            "/api/v1/products/",
            {"page": 4, "per_page": 10},
        )

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, '{"products": []}')
        self.assertEqual(len(products), 0)

    def test_get_data_pagination_beyond_beginning(self):
        response = self.client.get(
            "/api/v1/products/",
            {"page": 0, "per_page": 10},
        )

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, '{"products": []}')
        self.assertEqual(len(products), 0)

    def test_get_data_empty_search(self):
        response = self.client.get(
            "/api/v1/products/",
            {"search": ""},
        )

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, '{"products": []}')
        self.assertEqual(len(products), 0)

    def test_get_data_search_not_available(self):
        response = self.client.get(
            "/api/v1/products/",
            {"search": "Test Product 99"},
        )

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content, '{"products": []}')
        self.assertEqual(len(products), 0)

    def test_get_data_search(self):
        self.product = baker.make_recipe("retail_app.product_test_related")

        response = self.client.get(
            "/api/v1/products/",
            {"search": "some keywords to search for things in a string"},
        )

        content = response.content.decode("utf-8")

        products = json.loads(content)["products"]
        first_product_name = json.loads(products[0])["name"]

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(content, '{"products": []}')
        self.assertEqual(len(products), 1)
        self.assertEqual(first_product_name, "Test Product")
