from django.test import TestCase
from retail_app.models import Business
from model_bakery import baker


class BusinessTest(TestCase):
    """Business correctly returns attributes"""

    def setUp(self):
        self.business = baker.make_recipe("retail_app.business_test")

    def test_name(self):
        business = Business.objects.get(name="Test Business")

        self.assertEqual(business.name, "Test Business")

    def test_site_url(self):
        business = Business.objects.get(site_url="https://www.testsite.com")

        self.assertEqual(business.site_url, "https://www.testsite.com")
