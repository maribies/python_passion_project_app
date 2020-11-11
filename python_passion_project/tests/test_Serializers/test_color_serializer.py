from django.test import TestCase
from model_bakery import baker
from api.serializers import ColorSerializer


class TestColorSerializer(TestCase):
    def setUp(self):
        self.color = baker.make_recipe("retail_app.color_test")

    def test_to_dict(self):
        result = ColorSerializer(self.color).to_dict()

        self.assertEqual(result, "purple")
