from django.test import TestCase
from model_bakery import baker
from api.serializers import KeywordsSerializer


class TestKeywordsSerializer(TestCase):
    def setUp(self):
        self.keywords = baker.make_recipe("retail_app.search_test")

    def test_for_json(self):
        result = KeywordsSerializer(self.keywords).for_json()

        self.assertEqual(result, "some keywords to search for things in a string")
