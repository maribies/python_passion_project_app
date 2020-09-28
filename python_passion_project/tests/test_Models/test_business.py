from django.test import TestCase
from retail_app.models import Business
from model_bakery import baker


class BusinessTest(TestCase):
    """Business correctly returns attributes"""

    def setUp(self):
        self.business = baker.make_recipe("retail_app.business_test")

    def test_name(self):
        self.assertEqual(self.business.name, "Test Business")

    def test_site_url(self):
        self.assertEqual(self.business.site_url, "https://www.testsite.com")
