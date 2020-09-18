from django.test import TestCase
from retail_app.models import Collection
from model_bakery import baker


class CollectionTest(TestCase):
    """Collection correctly returns attribute"""

    def setUp(self):
        self.collection = baker.make_recipe("retail_app.collection_test")

    def test_name(self):
        self.assertEqual(self.collection.name, "Test Collection")
