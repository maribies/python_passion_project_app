from django.test import TestCase
from retail_app.models import ProductDescription
from model_bakery import baker


class ProductDescriptionTest(TestCase):
    """ProductDescription correctly returns attributes"""

    def setUp(self):
        self.category = baker.make_recipe("retail_app.description_test")

    def test_name(self):
        description = ProductDescription.objects.get(
            name="Test Product Description Name"
        )

        self.assertEqual(description.name, "Test Product Description Name")

    def test_season(self):
        description = ProductDescription.objects.get(season="SS20")

        self.assertEqual(description.season, "SS20")

    def test_collection(self):
        description = ProductDescription.objects.get(collection="Test Collection")

        self.assertEqual(description.collection, "Test Collection")

    def test_category(self):
        description = ProductDescription.objects.get(category="Handbags")

        self.assertEqual(description.category, "Handbags")

    def test_brand(self):
        description = ProductDescription.objects.get(brand="Test Brand")

        self.assertEqual(description.brand, "Test Brand")
