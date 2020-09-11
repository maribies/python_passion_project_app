from django.test import TestCase
from retail_app.models import BusinessDesigner


class BusinessDesignerTest(TestCase):
    """BusinessDesigner correctly returns name"""

    def setUp(self):
        BusinessDesigner.objects.create(name="Test Designer",)

    def test_name(self):
        designer = BusinessDesigner.objects.get(name="Test Designer")

        self.assertEqual(designer.name, "Test Designer")
