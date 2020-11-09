from django.test import RequestFactory, TestCase
from retail_app.views import search
from model_bakery import baker


class TestSearchView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.products = baker.make_recipe("retail_app.products_test", _quantity=21)

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

    def test_search_query_with_pages(self):
        self.product = baker.make_recipe("retail_app.product_test_related")

        request = self.factory.get("/search/?search=things&page=1")

        response = search(request)

        self.assertEqual(response.status_code, 200)
