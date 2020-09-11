from django.test import TestCase
from retail_app.models import Product, ProductDescription, ProductPrice, ProductDetails


class ProductTestCase(TestCase):
    """Products correctly return names"""
    def setUp(self):
        description = ProductDescription.objects.create(
          name="Test Product Description Name",
          season="SS20",
          collection="Test Collection",
          category="Handbags",
          brand="Test Brand"
        )

        price = ProductPrice.objects.create(
          currency="$",
          amount=1234.56
        )

        details = ProductDetails.objects.create(
          material="test materials made of lots of things",
          size="OS",
          dimensions="10in long and 18in wide and 3in depth",
          sku="TESTSKU89012",
        )

        Product.objects.create(
          name="Test Product",
          designer="Test Designer",
          product_description=description,
          product_price=price,
          site_url="https://www.testsite.com",
          product_details=details,
          condition="New",
        )

    def test_name(self):
        product = Product.objects.get(name="Test Product")

        self.assertEqual(product.name, "Test Product")
