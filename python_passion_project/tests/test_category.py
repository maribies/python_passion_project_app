from django.test import TestCase
from retail_app.models import Category
from model_bakery import baker


class CategoryTest(TestCase):
    """Cateogry correctly returns attribute"""

    def setUp(self):
        self.category = baker.make_recipe("retail_app.category_test")

    def test_name(self):
        category = Category.objects.get(name="Test Category")

        self.assertEqual(category.name, "Test Category")
