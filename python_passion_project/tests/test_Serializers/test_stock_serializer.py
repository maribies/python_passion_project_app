from django.test import TestCase
from model_bakery import baker
from api.serializers import StockSerializer
import json


class TestStockSerializer(TestCase):
    def setUp(self):
        self.stock = baker.make_recipe("retail_app.stock_test")

    def test_to_json(self):
        result = StockSerializer(self.stock).to_json()

        self.assertEqual(result, {"color": "purple", "quantity": 1})
