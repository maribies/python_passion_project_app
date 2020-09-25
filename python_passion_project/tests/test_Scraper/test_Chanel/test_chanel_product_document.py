from django.test import TestCase
from scraping import ChanelHtml, ChanelProductDocument
import re


class ChanelProductDocumentsTest(TestCase):
    def setUp(self):
        self.url = "https://www.chanel.com/us/fashion/p/AS2189B04424N9307/small-flap-bag-lambskin-gold-tone-metal"
        self.html = ChanelHtml.get_html_data(self, self.url)
        self.product = ChanelProductDocument(self.html)

    # Given a url, check that url scraping returns the correct html data
    # by asserting the title matches the data requested.
    # Don't think need to test all bc of check for unique and it's the same logic for all.
    def test_products_get_product_html(self):
        # product_urls = self.chanel.get_product_urls(pages=3)

        # url = product_urls.pop()

        title = ChanelProductDocument.page_title(self.html)

        clean_title_words = re.split(r"\W+", title)

        clean_url_words = self.url.split("-")
        del clean_url_words[0]

        for word in clean_url_words:
            word = word.capitalize()

            if word.endswith("quickview"):
                word = word.strip("/quickview")

            if word == "With":
                word = word.lower()

            self.assertIn(word, clean_title_words)

    # New test for error and bad url with expectation of failure

    # Given html data, check that data needed can be parsed.
    # name, description (season, collection, category, brand), price, details (material, size, dimension, sku)
    # color, (quantity will be assumed in stock), images
