from django.test import TestCase
from retail_app.models import ProductStock
from model_bakery import baker


class ProductStockTest(TestCase):
    """ProductStock correctly returns attributes"""

    def setUp(self):
        self.stock = baker.make_recipe("retail_app.stock_test")

    def test_quantity(self):
        self.assertEqual(self.stock.quantity, 1)

    def test_product(self):
        self.assertEqual(self.stock.product.name, "Test Product")

    def test_color(self):
        self.assertEqual(self.stock.color.color, "purple")
