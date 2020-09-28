from django.test import TestCase
from scraping import ChanelHtml, ChanelProductDocument
import re


class TestChanelProductDocuments(TestCase):
    def setUp(self):
        self.product_info = {
            "url": "https://www.chanel.com/us/fashion/p/A01112Y0129594305/classic-handbag-lambskin-gold-tone-metal",
            "id": "A01112Y0129594305",
            "collection_season": "reorders",
        }
        self.html = ChanelHtml.get_html_data(self, self.product_info.get("url"))
        self.product = ChanelProductDocument(self.html)

    # Given a url, check that url scraping returns the correct html data
    # by asserting the title matches the data requested.
    # Don't think need to test all bc of check for unique and it's the same logic for all.
    def test_products_get_product_html(self):
        title = ChanelProductDocument.page_title(self.html)

        clean_title_words = re.split(r"\W+", title)
        clean_url_words = self.product_info.get("url").split("-")
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
    def test_product_dimensions(self):
        dimensions = ChanelProductDocument.product_dimensions(self.html)

        assert dimensions != ""
        assert dimensions is not None
        self.assertIsInstance(dimensions, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(dimensions, "6 × 9.9 × 2.5 in")

    def test_product_amount(self):
        amount = ChanelProductDocument.product_amount(self.html)

        assert amount != ""
        assert amount is not None
        self.assertIsInstance(amount, float)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(amount, 6_500)

    def test_product_currency(self):
        currency = ChanelProductDocument.product_currency(self)

        assert currency != ""
        assert currency is not None
        self.assertIsInstance(currency, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(currency, "$")

    def test_product_images(self):
        images = ChanelProductDocument.product_images(self)

        assert images != []
        assert images is not None
        self.assertIsInstance(images[0], str)
        self.assertIsInstance(images, list)

    def test_product_material(self):
        material = ChanelProductDocument.product_material(self)

        assert material != ""
        assert material is not None
        self.assertIsInstance(material, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(material, "Lambskin & Gold-Tone Metal")

    def test_product_color(self):
        color = ChanelProductDocument.product_color(self)

        assert color != ""
        assert color is not None
        self.assertIsInstance(color, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(color, "Black")

    def test_products_get_name(self):
        name = ChanelProductDocument.product_name(self)

        assert name != ""
        assert name is not None
        self.assertIsInstance(name, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(name, "Classic Handbag Lambskin & Gold-Tone Metal")

    # TODO: Add test for product like https://www.chanel.com/us/fashion/p/AS1941B03709N4738/evening-bag-lambskin-enamel-strass-gold-tone-metal/ with price upon request.
