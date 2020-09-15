from django.test import TestCase
from retail_app.models import ProductDetails


class ProductDetailsTest(TestCase):
    """ProductDetails correctly returns sku"""

    def setUp(self):
        ProductDetails.objects.create(
            material="test materials made of lots of things",
            size="OS",
            dimensions="10in long and 18in wide and 3in depth",
            sku="TESTSKU89012",
        )

    def test_sku(self):
        details = ProductDetails.objects.get(sku="TESTSKU89012")

        self.assertEqual(details.sku, "TESTSKU89012")

    def test_material(self):
        details = ProductDetails.objects.get(
            material="test materials made of lots of things"
        )

        self.assertEqual(details.material, "test materials made of lots of things")

    def test_size(self):
        details = ProductDetails.objects.get(size="OS")

        self.assertEqual(details.size, "OS")

    def test_dimensions(self):
        details = ProductDetails.objects.get(
            dimensions="10in long and 18in wide and 3in depth"
        )

        self.assertEqual(details.dimensions, "10in long and 18in wide and 3in depth")
