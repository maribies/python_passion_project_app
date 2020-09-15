from django.test import TestCase
from retail_app.models import (
    SearchProductKeywords,
    Product,
    ProductDescription,
    ProductDetails,
    ProductPrice,
)


class SearchProductKeywordsTest(TestCase):
    """SearchProductKeywords correctly returns attributes and creates keywords"""

    def setUp_product(self):
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

        return product

    def setUp(self):
        product = SearchProductKeywordsTest.setUp_product(self)
        SearchProductKeywords.objects.create(
            product=product, keywords="some keywords to search for things in a string"
        )

    def test_keywords(self):
        search = SearchProductKeywords.objects.get(product=1)

        self.assertEqual(
            search.keywords, "some keywords to search for things in a string"
        )

    def test_product(self):
        search = SearchProductKeywords.objects.get(product=1)

        self.assertEqual(search.product.name, "Test Product")

    def test_keywords_create(self):
        product = SearchProductKeywordsTest.setUp_product(self)

        product_data = {
            "product_details": {"sku": "123testsku12"},
            "product_description": {
                "name": "test data name",
                "season": "ss20",
                "collection": "test collection",
                "brand": "test brand",
            },
            "designer": "test designer",
            "stock": {"colors": ["purple", "black", "gunmetal"]},
        }

        SearchProductKeywords.create_keywords(product_data, product)
        search = SearchProductKeywords.objects.get(product=2)

        self.assertEqual(
            search.keywords,
            "123testsku12 test data name ss20 test collection test brand test designer purple black gunmetal",
        )
