from django.test import TestCase
from retail_app.models import (
    ProductStock,
    Product,
    ProductDescription,
    ProductDetails,
    ProductPrice,
    ProductColor,
)


class ProductStockTest(TestCase):
    """ProductStock correctly returns quantity"""

    def setUp(self):
        description = ProductDescription.objects.create(
            name="Test Product Description Name",
            season="SS20",
            collection="Test Collection",
            category="Handbags",
            brand="Test Brand",
        )

        price = ProductPrice.objects.create(currency="$", amount=1234.56)

        details = ProductDetails.objects.create(
            material="test materials made of lots of things",
            size="OS",
            dimensions="10in long and 18in wide and 3in depth",
            sku="TESTSKU89012",
        )

        product = Product.objects.create(
            name="Test Product",
            designer="Test Designer",
            product_description=description,
            product_price=price,
            site_url="https://www.testsite.com",
            product_details=details,
            condition="New",
        )

        color = ProductColor.objects.create(color="purple")

        ProductStock.objects.create(product=product, color=color, quantity=1)

    def test_quantity(self):
        stock = ProductStock.objects.get(quantity=1)

        self.assertEqual(stock.quantity, 1)

    def test_product(self):
        stock = ProductStock.objects.get(product=1)

        self.assertEqual(stock.product.name, "Test Product")

    def test_color(self):
        stock = ProductStock.objects.get(color=1)

        self.assertEqual(stock.color.color, "purple")
