from django.test import TestCase
from scraping import CreateDesigner
from retail_app.models import Designer


class TestCreateDesigner(TestCase):
    def setUp(self):
        self.name = "Issey Miyake"
        self.url = "https://www.shopbaobaoisseymiyake.com/"

    def test_create_designer(self):
        designer = CreateDesigner(self.name, self.url)

        self.assertIsInstance(designer, CreateDesigner)
        self.assertEqual(type(designer.name), str)
        self.assertEqual(type(designer.url), str)
        self.assertEqual(designer.name, "Issey Miyake")
        self.assertEqual(designer.url, "https://www.shopbaobaoisseymiyake.com/")
