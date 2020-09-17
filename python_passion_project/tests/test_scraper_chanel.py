from django.test import TestCase
from scraping import get_chanel


class ChanelScraperTest(TestCase):
    """Test the Chanel Scraper"""

    def setUp(self):
        # Run the scraper to get the data.
        self.site_html_data = get_chanel.get_site_data()
        self.first_page_products_data = get_chanel.get_products()
        self.second_page_products = get_chanel.check_products_next_page()
        self.total_results = get_chanel.get_total_results()
        self.last_page = get_chanel.check_last_page()

    def test_html_page_data(self):
        # Check that there is data.
        assert self.site_html_data is not None

    def test_products_request_first_page(self):
        # Check data is received from the request.
        assert self.first_page_products_data is not None

    def test_products_request_next_page(self):
        # Check for a next page and receive data from the request.
        self.assertIn("page=2", self.second_page_products)

    # Check to receive page data until the end.
    # We can get total results and we also know that the request returns 24 elements,
    # So we should be able to get the last page by dividing the total by 24
    # Ie 217 products/24 per page= 9.04 => 10 pages and next should be 0
    def test_products_request_last_page(self):
        self.assertEqual("", self.last_page)
