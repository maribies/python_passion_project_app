from django.test import TestCase
from retail_app.models import ProductPrice
from decimal import Decimal
from model_bakery import baker


class ProductPriceTest(TestCase):
    """ProductPrice correctly returns attributes"""

    def setUp(self):
        self.price = baker.make_recipe("retail_app.price_test")

    def test_currency(self):
        self.assertEqual(self.price.currency, "$")

    def test_amount(self):
        self.assertEqual(self.price.amount, Decimal("1234.56"))
