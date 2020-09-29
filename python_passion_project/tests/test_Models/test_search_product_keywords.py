from django.test import TestCase
from retail_app.models import SearchProductKeywords
from model_bakery import baker


class SearchProductKeywordsTest(TestCase):
    """SearchProductKeywords correctly returns attributes and creates keywords"""

    def setUp(self):
        self.search = baker.make_recipe("retail_app.search_test")

    def test_keywords(self):
        self.assertEqual(
            self.search.keywords, "some keywords to search for things in a string"
        )

    def test_product(self):
        self.assertEqual(self.search.product.name, "Test Product")

    def test_keywords_create(self):
        product = baker.make_recipe("retail_app.product_test")

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
        search = SearchProductKeywords.objects.get(
            keywords="123testsku12 test data name ss20 test collection test brand test designer purple black gunmetal"
        )

        self.assertEqual(
            search.keywords,
            "123testsku12 test data name ss20 test collection test brand test designer purple black gunmetal",
        )
