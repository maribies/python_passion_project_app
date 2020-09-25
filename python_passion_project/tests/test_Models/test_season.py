from django.test import TestCase
from retail_app.models import Season
from model_bakery import baker


class SeasonTest(TestCase):
    """Season correctly returns attribute"""

    def setUp(self):
        self.season = baker.make_recipe("retail_app.season_test")

    def test_name(self):
        self.assertEqual(self.season.name, "SS20")
