from django.test import TestCase
from retail_app.models import ProductColor


class ProductColorTest(TestCase):
    """ProductColor correctly returns color"""

    def setUp(self):
        ProductColor.objects.create(color="purple")

    def test_color(self):
        color = ProductColor.objects.get(color="purple")

        self.assertEqual(color.color, "purple")
