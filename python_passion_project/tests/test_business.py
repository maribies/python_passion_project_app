from django.test import TestCase
from retail_app.models import Business, BusinessDesigner, Category


class BusinessTest(TestCase):
    """Business correctly returns attributes"""

    def setUp(self):
        designer = BusinessDesigner.objects.create(
            name="Test Designer",
        )

        category = Category.objects.create(
            name="Test Designer",
        )

        Business.objects.create(
            name="Test Product",
            site_url="https://www.testsite.com",
            designer=designer,
            category=category,
        )

    def test_name(self):
        business = Business.objects.get(name="Test Product")

        self.assertEqual(business.name, "Test Product")

    def test_site_url(self):
        business = Business.objects.get(site_url="https://www.testsite.com")

        self.assertEqual(business.site_url, "https://www.testsite.com")
