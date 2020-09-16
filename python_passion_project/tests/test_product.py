from django.test import TestCase
from retail_app.models import Product
from model_bakery import baker


class ProductTest(TestCase):
    """Product correctly returns attributes"""

    def setUp(self):
        self.product = baker.make_recipe("retail_app.product_test")

    def test_name(self):
        product = Product.objects.get(name="Test Product")

        self.assertEqual(product.name, "Test Product")

    def test_designer(self):
        product = Product.objects.get(designer="Test Designer")

        self.assertEqual(product.designer, "Test Designer")

    def test_site_url(self):
        product = Product.objects.get(site_url="https://www.testsite.com")

        self.assertEqual(product.site_url, "https://www.testsite.com")

    def test_condition(self):
        product = Product.objects.get(condition="New")

        self.assertEqual(product.condition, "New")
