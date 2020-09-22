from django.test import TestCase
from scraping import get_chanel
import urllib.request
import re


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

    # Check that each product page has data- head request
    def test_products_request_all(self):
        for page in get_chanel.generate_pages():
            products_data = get_chanel.get_products(page)

            assert products_data is not None

    # Request data does have url (24 unique, it seems),
    # seems to be organized by id with color code with the id field being the root id
    # the following seem to have 96, each one listed 4 times,
    # id, price, currency code
    # dimension18, whichappears to be season information,
    # variant seems to be color way
    # name will need to be cleaned from description and color info
    # images are in messy data at the end of the file

    # not in request:
    # dimension information (at least not readable)

    # Because all info isn't in request, use as index, like bao bao.

    # assumptions/default - stock will be null

    # Get unique product page and make sure each is unique and valid.
    def test_products_get_urls_one_page(self):
        product_urls = get_chanel.get_product_urls(pages=1)

        # Urls should be unique and there should be 24 results
        set_of_urls = set(product_urls)
        self.assertEqual(len(set_of_urls), len(product_urls))
        self.assertEqual(len(product_urls), 24)

    def test_products_get_urls_pages(self):
        number_of_pages = 3

        product_urls = get_chanel.get_product_urls(pages=number_of_pages)

        # Urls should be unique and there should be 24 results per page,
        # with the exception of the last page, so don't test until last page/
        # TODO: update last assertion to make more robust.
        set_of_urls = set(product_urls)
        self.assertEqual(len(set_of_urls), len(product_urls))
        self.assertEqual(len(product_urls), number_of_pages * 24)

    def test_products_open_product_url(self):
        product_urls = get_chanel.get_product_urls(pages=2)

        url = product_urls.pop()

        req = url.test_request()

        try:
            response = url.test_open_url(req)

            path = url.test_get_path(response)

            self.assertEqual(url.url_path, path + "quickview")

        except url.test_url_error():
            raise AssertionError

    # Given a url, check that url scraping returns data
    # - the title is the data requested.
    # Don't think need to test all bc of check for unique and it's the same logic for all.
    def test_products_get_product_html(self):
        product_urls = get_chanel.get_product_urls(pages=3)

        url = product_urls.pop()

        html = get_chanel.get_product_html(url.url_path)

        title = html.test_page_title()

        clean_title_words = re.split(r"\W+", title)

        clean_url_words = url.url_path.split("-")
        del clean_url_words[0]

        for word in clean_url_words:
            word = word.capitalize()

            if word.endswith("quickview"):
                word = word.strip("/quickview")

            if word == "With":
                word = word.lower()

            self.assertIn(word, clean_title_words)
