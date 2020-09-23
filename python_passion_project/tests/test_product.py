from django.test import TestCase
from retail_app.models import Product
from model_bakery import baker


class ProductTest(TestCase):
    """Product correctly returns attributes"""

    def setUp(self):
        self.product = baker.make_recipe("retail_app.product_test")

    def test_name(self):
        self.assertEqual(self.product.name, "Test Product")

    def test_designer(self):
        self.assertEqual(self.product.designer, "Test Designer")

    def test_site_url(self):
        self.assertEqual(self.product.site_url, "https://www.testsite.com")

    def test_condition(self):
        self.assertEqual(self.product.condition, "New")

    def test_sku(self):
        self.assertEqual(self.product.sku, "TESTSKU89012")

    def test_material(self):
        self.assertEqual(self.product.material, "test materials made of lots of things")

    def test_size(self):
        self.assertEqual(self.product.size, "OS")

    def test_dimensions(self):
        self.assertEqual(
            self.product.dimensions, "10in long and 18in wide and 3in depth"
        )

    def test_season(self):
        self.assertEqual(self.product.season, "SS20")

    def test_collection(self):
        self.assertEqual(self.product.collection, "Test Collection")

    def test_category(self):
        self.assertEqual(self.product.category, "Handbags")

    def test_brand(self):
        self.assertEqual(self.product.brand, "Test Brand")
