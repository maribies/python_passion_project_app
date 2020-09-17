from django.test import TestCase
from retail_app.models import Category


class CategoryTest(TestCase):
    """Cateogry correctly returns name"""

    def setUp(self):
        Category.objects.create(
            name="Test Category",
        )

    def test_name(self):
        category = Category.objects.get(name="Test Category")

        self.assertEqual(category.name, "Test Category")
