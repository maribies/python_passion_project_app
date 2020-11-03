from django.test import TestCase
from model_bakery import baker
from api.serializers import PriceSerializer


class TestPriceSerializer(TestCase):
    def setUp(self):
        self.price = baker.make_recipe("retail_app.price_test")

    def test_for_json(self):
        result = PriceSerializer(self.price).for_json()

        self.assertEqual(result, "$1234.56")
