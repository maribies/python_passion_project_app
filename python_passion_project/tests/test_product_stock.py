from django.test import TestCase
from retail_app.models import ProductStock
from model_bakery import baker


class ProductStockTest(TestCase):
    """ProductStock correctly returns attributes"""

    def setUp(self):
        self.stock = baker.make_recipe("retail_app.stock_test")

    def test_quantity(self):
        stock = ProductStock.objects.get(quantity=1)

        self.assertEqual(stock.quantity, 1)

    def test_product(self):
        stock = ProductStock.objects.get(product=1)

        self.assertEqual(stock.product.name, "Test Product")

    def test_color(self):
        stock = ProductStock.objects.get(color=1)

        self.assertEqual(stock.color.color, "purple")
