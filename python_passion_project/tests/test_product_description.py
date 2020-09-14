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
