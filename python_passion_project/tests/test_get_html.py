from django.test import TestCase
from scraping import GetHTML


class GetHTMLTest(TestCase):
    def setUp(self):
        self.url = "https://www.chanel.com/us/fashion/handbags/c/1x1x1/"

    def test_get_html_data(self):
        html_data = GetHTML.get_html_data(self.url)

        assert html_data is not None
