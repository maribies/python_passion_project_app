from django.test import TestCase
from model_bakery import baker
from api.serializers import ProductSerializer
import json


class TestProductSerializer(TestCase):
    # To see entire error trace back for long assertions.
    maxDiff = None

    def setUp(self):
        self.product = baker.make_recipe("retail_app.product_test_related")
        self.product_empty_related = baker.make_recipe("retail_app.product_test")
        self.product_related_multiple = baker.make_recipe(
            "retail_app.product_test_related_multiples"
        )

    def test_product_stock(self):
        result_empty = ProductSerializer(self.product_empty_related).product_stock()
        result = ProductSerializer(self.product).product_stock()

        self.assertEqual(len(result_empty), 0)
        self.assertNotEqual(len(result), 0)

    def test_product_images(self):
        result_empty = ProductSerializer(self.product_empty_related).product_images()
        result = ProductSerializer(self.product).product_images()

        self.assertEqual(len(result_empty), 0)
        self.assertNotEqual(len(result), 0)

    def test_to_json(self):
        result = ProductSerializer(self.product).to_json()

        self.assertEqual(
            result,
            json.dumps(
                {
                    "name": "Test Product",
                    "designer": "Test Designer",
                    "site_url": "https://www.testsite.com",
                    "condition": "New",
                    "season": "SS20",
                    "collection": "Test Collection",
                    "category": "Handbags",
                    "brand": "Test Brand",
                    "material": "test materials made of lots of things",
                    "size": "OS",
                    "dimensions": "10in long and 18in wide and 3in depth",
                    "sku": "TESTSKU89012",
                    "product_price": "$1234.56",
                    "stock": [{"color": "purple", "quantity": 1}],
                    "images": ["https://www.imageurl.jpeg"],
                }
            ),
        )

    def test_to_json_empties(self):
        result = ProductSerializer(self.product_empty_related).to_json()

        self.assertEqual(
            result,
            json.dumps(
                {
                    "name": "Test Product",
                    "designer": "Test Designer",
                    "site_url": "https://www.testsite.com",
                    "condition": "New",
                    "season": "SS20",
                    "collection": "Test Collection",
                    "category": "Handbags",
                    "brand": "Test Brand",
                    "material": "test materials made of lots of things",
                    "size": "OS",
                    "dimensions": "10in long and 18in wide and 3in depth",
                    "sku": "TESTSKU89012",
                    "product_price": "$1234.56",
                    "stock": [],
                    "images": [],
                }
            ),
        )

    def test_to_json_multiples(self):
        result = ProductSerializer(self.product_related_multiple).to_json()

        self.assertEqual(
            result,
            json.dumps(
                {
                    "name": "Test Product",
                    "designer": "Test Designer",
                    "site_url": "https://www.testsite.com",
                    "condition": "New",
                    "season": "SS20",
                    "collection": "Test Collection",
                    "category": "Handbags",
                    "brand": "Test Brand",
                    "material": "test materials made of lots of things",
                    "size": "OS",
                    "dimensions": "10in long and 18in wide and 3in depth",
                    "sku": "TESTSKU89012",
                    "product_price": "$1234.56",
                    "stock": [
                        {"color": "purple", "quantity": 1},
                        {"color": "blue", "quantity": 4},
                    ],
                    "images": [
                        "https://www.imageurl.jpeg",
                        "https://www.imageurl2.jpeg",
                    ],
                }
            ),
        )
