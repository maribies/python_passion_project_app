from django.test import TestCase
from retail_app.models import Collection


class CollectionTest(TestCase):
    """Collection correctly returns name"""

    def setUp(self):
        Collection.objects.create(
            name="Test Collection",
        )

    def test_name(self):
        collection = Collection.objects.get(name="Test Collection")

        self.assertEqual(collection.name, "Test Collection")
