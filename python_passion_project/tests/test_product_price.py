from django.test import TestCase
from retail_app.models import ProductPrice
from decimal import Decimal


class ProductPriceTest(TestCase):
    """ProductPrice correctly returns currency and amount"""

    def setUp(self):
        ProductPrice.objects.create(currency="$", amount=Decimal("1234.56"))

    def test_currency(self):
        price = ProductPrice.objects.get(currency="$")

        self.assertEqual(price.currency, "$")

    def test_amount(self):
        price = ProductPrice.objects.get(currency="$")

        self.assertEqual(price.amount, Decimal("1234.56"))
