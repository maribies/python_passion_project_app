from django.test import TestCase
from retail_app.models import Designer


class DesignerTest(TestCase):
    """Designer correctly returns attributes"""

    def setUp(self):
        Designer.objects.create(
            name="Test Designer", site_url="https://www.testdesignersite.com"
        )

    def test_name(self):
        designer = Designer.objects.get(name="Test Designer")

        self.assertEqual(designer.name, "Test Designer")

    def test_site_url(self):
        designer = Designer.objects.get(site_url="https://www.testdesignersite.com")

        self.assertEqual(designer.site_url, "https://www.testdesignersite.com")
