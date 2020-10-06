from django.test import TestCase
from scraping import BaoBaoHtml, BaoBaoProductDocument
import re


class TestBaoBaoProductDocuments(TestCase):
    def setUp(self):
        self.product_info = {
            "url": "https://us-store.isseymiyake.com/collections/baobao/products/lucent-matte-crossbody-bag?variant=32170657579102"
        }
        self.html = BaoBaoHtml.get_html_data(self, self.product_info.get("url"))
        self.product = BaoBaoProductDocument(self.html)

    # Given html data, check that data needed can be parsed.
    # name, description (season, collection, category, brand), price, details (material, size, dimension, sku)
    # color, quantity, images
    def test_products_get_name(self):
        name = BaoBaoProductDocument.product_name(self)

        self.assertNotEqual(name, "")
        self.assertNotEqual(name, None)
        self.assertIsInstance(name, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(name, "LUCENT MATTE CROSSBODY BAG")

    def test_product_amount(self):
        amount = BaoBaoProductDocument.product_amount(self.html)

        self.assertNotEqual(amount, "")
        self.assertNotEqual(amount, None)
        self.assertIsInstance(amount, float)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(amount, 565)

    def test_product_currency(self):
        currency = BaoBaoProductDocument.product_currency(self.html)

        self.assertNotEqual(currency, "")
        self.assertNotEqual(currency, None)
        self.assertIsInstance(currency, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(currency, "$")

    def test_product_material(self):
        material = BaoBaoProductDocument.product_material(self.html)

        self.assertNotEqual(material, "")
        self.assertNotEqual(material, None)
        self.assertIsInstance(material, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(
            material,
            "Surface: Vinyl chloride resin / Base cloth: 100% polyester / Lining: 100% nylon / Tape: 100% nylon / Part: Artificial leather",
        )

    def test_product_sku(self):
        sku = BaoBaoProductDocument.product_sku(self.html)

        self.assertNotEqual(sku, "")
        self.assertNotEqual(sku, None)
        self.assertIsInstance(sku, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(sku, "BB08AG685")

    def test_product_colors(self):
        color = BaoBaoProductDocument.product_colors(self.html)

        self.assertNotEqual(color, [])
        self.assertNotEqual(color, None)
        self.assertIsInstance(color, list)
        self.assertEqual(type(color[0]), str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(color, ["Light Gray", "Gray", "Black"])

    def test_product_images(self):
        images = BaoBaoProductDocument.product_images(self.html)

        self.assertNotEqual(images, [])
        self.assertNotEqual(images, None)
        self.assertIsInstance(images, list)
        self.assertEqual(type(images[0]), str)

    def test_product_dimensions_none(self):
        dimensions = BaoBaoProductDocument.product_dimensions(self.html)

        self.assertNotEqual(dimensions, None)
        self.assertIsInstance(dimensions, str)
        self.assertNotEqual(dimensions, "")
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(dimensions, "Unavailable")

    def test_product_dimensions(self):
        html = BaoBaoHtml.get_html_data(
            self, "https://us-store.isseymiyake.com/products/wring-crossbody-bag"
        )

        dimensions = BaoBaoProductDocument.product_dimensions(html)

        self.assertNotEqual(dimensions, None)
        self.assertIsInstance(dimensions, str)
        self.assertNotEqual(dimensions, "")
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(dimensions, "9.3 in x 9.3 in x 3.1 in")
