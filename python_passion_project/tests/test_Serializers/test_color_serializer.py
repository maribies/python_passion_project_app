from django.test import TestCase
from model_bakery import baker
from retail_app.serializers import ColorSerializer


class TestColorSerializer(TestCase):
    def setUp(self):
        self.color = baker.make_recipe("retail_app.color_test")

    def test_to_json(self):
        result = ColorSerializer(self.color).for_json()

        self.assertEqual(result, "purple")
