from django.test import TestCase
from retail_app.models import ProductDescription


class ProductDescriptionTest(TestCase):
    """ProductDescription correctly returns name"""

    def setUp(self):
        ProductDescription.objects.create(
            name="Test Product Description Name",
            season="SS20",
            collection="Test Collection",
            category="Handbags",
            brand="Test Brand",
        )

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
