from django.test import TestCase
from retail_app.models import Product


class TestProductsManager(TestCase):
    def test_fully_loaded_objects(self):
        products = Product.objects.fully_loaded_objects()

        self.assertNotEqual(products, None)
        self.assertNotEqual(products.first, None)
