from django.test import TestCase
from model_bakery import baker
from api.serializers import ImageSerializer


class TestImageSerializer(TestCase):
    def setUp(self):
        self.image = baker.make_recipe("retail_app.image_test")

    def test_to_dict(self):
        result = ImageSerializer(self.image).to_dict()

        self.assertEqual(result, "https://www.imageurl.jpeg")
