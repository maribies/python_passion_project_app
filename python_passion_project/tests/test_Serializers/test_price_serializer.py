from django.test import TestCase
from model_bakery import baker
from api.serializers import PriceSerializer


class TestPriceSerializer(TestCase):
    def setUp(self):
        self.price = baker.make_recipe("retail_app.price_test")

    def test_to_dict(self):
        result = PriceSerializer(self.price).to_dict()

        self.assertEqual(result, "$1234.56")
