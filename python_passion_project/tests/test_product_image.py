from django.test import TestCase
from retail_app.models import ProductImage
from model_bakery import baker


class ProductImageTest(TestCase):
    """ProductImage correctly returns attributes"""

    def setUp(self):
        self.image = baker.make_recipe("retail_app.image_test")

    def test_url(self):
        self.assertEqual(self.image.image_url, "https://www.imageurl.jpeg")

    def test_product(self):
        self.assertEqual(self.image.product.name, "Test Product")
