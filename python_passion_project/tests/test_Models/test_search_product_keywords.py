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
