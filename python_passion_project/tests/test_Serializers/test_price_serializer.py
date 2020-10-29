from django.test import TestCase
from model_bakery import baker
from retail_app.serializers import PriceSerializer


class TestPriceSerializer(TestCase):
    def setUp(self):
        self.price = baker.make_recipe("retail_app.price_test")

    def test_to_json(self):
        result = PriceSerializer(self.price).to_json()

        self.assertEqual(result, "$1234.56")
