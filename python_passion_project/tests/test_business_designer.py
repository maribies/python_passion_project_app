from django.test import TestCase
from retail_app.models import BusinessDesigner
from model_bakery import baker


class BusinessDesignerTest(TestCase):
    """BusinessDesigner correctly returns attribute"""

    def setUp(self):
        self.business_designer = baker.make_recipe("retail_app.business_designer_test")

    def test_name(self):
        self.assertEqual(self.business_designer.name, "Test Designer")
