from django.test import TestCase
from retail_app.models import (
    ProductImage,
    Product,
    ProductDescription,
    ProductDetails,
    ProductPrice,
)


class ProductImageTest(TestCase):
    """ProductImage correctly returns url"""

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

        ProductImage.objects.create(
            product=product, image_url="https://www.imageurl.jpeg"
        )

    def test_url(self):
        image = ProductImage.objects.get(image_url="https://www.imageurl.jpeg")

        self.assertEqual(image.image_url, "https://www.imageurl.jpeg")

    def test_product(self):
        image = ProductImage.objects.get(product=1)

        self.assertEqual(image.product.name, "Test Product")
