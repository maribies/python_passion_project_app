from django.test import TestCase
from scraping import DesignerChanel
import urllib.request
import re
from .test_url import UrlTest


class ChanelScraperTest(TestCase):
    """Test the Chanel Scraper"""

    def setUp(self):
        self.chanel = DesignerChanel()
        self.url = UrlTest()

    def test_html_page_data(self):
        # Check that there is data.
        assert self.chanel.get_site_data() is not None

    def test_products_request_first_page(self):
        # Check data is received from the request.
        assert self.chanel.get_products() is not None

    def test_products_request_next_page(self):
        # Check for a next page and receive data from the request.
        page_url = self.chanel.check_products_next_page()

        self.assertIn("page=2", page_url)

    # Check to receive page data until the end.
    # We can get total results and we also know that the request returns 24 elements,
    # So we should be able to get the last page by dividing the total by 24
    # Ie 217 products/24 per page= 9.04 => 10 pages and next should be 0
    def test_products_request_last_page(self):
        last_page = self.chanel.check_last_page()

        self.assertEqual("", last_page)

    # Check that each product page has data- head request
    def test_products_request_all(self):
        for page in self.chanel.generate_pages():
            products_data = self.chanel.get_products(page)

            assert products_data is not None

    # Get unique product page and make sure each is unique and valid.
    def test_products_get_urls_one_page(self):
        product_urls = self.chanel.get_product_urls(pages=1)

        # Urls should be unique and there should be 24 results
        set_of_urls = set(product_urls)
        self.assertEqual(len(set_of_urls), len(product_urls))
        self.assertEqual(len(product_urls), 24)

    def test_products_get_urls_pages(self):
        number_of_pages = 3

        product_urls = self.chanel.get_product_urls(pages=number_of_pages)

        # Urls should be unique and there should be 24 results per page,
        # with the exception of the last page, so don't test until last page/
        # TODO: update last assertion to make more robust.
        set_of_urls = set(product_urls)
        self.assertEqual(len(set_of_urls), len(product_urls))
        self.assertEqual(len(product_urls), number_of_pages * 24)

    # Given a url, it should open the correct page.
    def test_products_open_product_url(self):
        product_urls = self.chanel.get_product_urls(pages=2)

        url = product_urls.pop()

        req = self.url.request(url)

        try:
            response = self.url.open_url(req)

            path = self.url.get_path(response)

            self.assertEqual(url, path + "quickview")

        except self.url.url_error():
            raise AssertionError

    # Given a url, check that url scraping returns the correct html data
    # by asserting the title matches the data requested.
    # Don't think need to test all bc of check for unique and it's the same logic for all.
    def test_products_get_product_html(self):
        product_urls = self.chanel.get_product_urls(pages=3)

        url = product_urls.pop()

        html = self.chanel.get_product_html(url)

        title = html.page_title()

        clean_title_words = re.split(r"\W+", title)

        clean_url_words = url.split("-")
        del clean_url_words[0]

        for word in clean_url_words:
            word = word.capitalize()

            if word.endswith("quickview"):
                word = word.strip("/quickview")

            if word == "With":
                word = word.lower()

            self.assertIn(word, clean_title_words)

    # Given html data, check that data needed can be parsed.
    # name, description (season, collection, category, brand), price, details (material, size, dimension, sku)
    # color, (quantity will be assumed in stock), images
