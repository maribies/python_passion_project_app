from django.test import TestCase
from retail_app.models import ProductColor
from model_bakery import baker


class ProductColorTest(TestCase):
    """ProductColor correctly returns attribute"""

    def setUp(self):
        self.color = baker.make_recipe("retail_app.color_test")

    def test_color(self):
        self.assertEqual(self.color.color, "purple")
