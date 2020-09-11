from django.test import TestCase
from retail_app.models import Season


class SeasonTest(TestCase):
    """Season correctly returns color"""

    def setUp(self):
        Season.objects.create(name="SS20")

    def test_name(self):
        season = Season.objects.get(name="SS20")

        self.assertEqual(season.name, "SS20")
