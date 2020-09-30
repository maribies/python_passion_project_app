from django.test import RequestFactory, TestCase
from retail_app.views import search


class SearchView(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_search(self):
        # Create an instance of a GET request.
        request = self.factory.get("/search")

        # Recall that middleware are not supported. You can simulate by setting manually.
        request.query = "black"

        # Test my_view() as if it were deployed at /customer/details
        response = search(request)

        self.assertEqual(response.status_code, 200)
