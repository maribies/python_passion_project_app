from django.test import TestCase
from retail_app.models import Category
from model_bakery import baker


class CategoryTest(TestCase):
    """Category correctly returns attribute"""

    def setUp(self):
        self.category = baker.make_recipe("retail_app.category_test")

    def test_name(self):
        self.assertEqual(self.category.name, "Test Category")
