from django.test import RequestFactory, TestCase
from retail_app.views import search


class TestSearchView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_search_color(self):
        request = self.factory.get("/search")

        request.query = "black"

        response = search(request)

        self.assertEqual(response.status_code, 200)

    def test_search_blank(self):
        request = self.factory.get("/search")

        request.query = " "

        response = search(request)

        self.assertEqual(response.status_code, 200)
