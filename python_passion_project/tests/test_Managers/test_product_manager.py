from django.test import TestCase
from retail_app.models import Product
from model_bakery import baker


class TestProductsManager(TestCase):
    def setUp(self):
        self.product = baker.make_recipe("retail_app.product_test")

    def test_fully_loaded_objects(self):
        products = Product.objects.fully_loaded_objects()

        self.assertNotEqual(products, None)
        self.assertNotEqual(products.first, None)

    def test_stock_ojects(self):
        products = Product.objects.stock_objects()

        self.assertNotEqual(products, None)
        self.assertNotEqual(products.first, None)
