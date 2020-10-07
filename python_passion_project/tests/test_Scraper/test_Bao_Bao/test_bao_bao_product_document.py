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
        self.description = "With it's drawstring closure and soft textured surface, WRING NUBUCK offers a contemporary take on the bucket bag design.This crossbody bag is complete with a single nylon cord that can be tied at multiple lengths, allowing for various ways to style and wear.Product Code: BB08-AG594Material: Polyurethane / Polyvinyl Chloride String: 100% NylonCare: Wipe gently with a damp, tightly wrung soft cloth, and then wipe dry.Dimensions: 9.4 x 6.3 x 3.1in"

    # Given html data, check that data needed can be parsed.
    # name, description (season, collection, category, brand), price, details (material, size, dimension, sku)
    # color, quantity, images
    def test_products_get_name(self):
        name = self.product.product_name()

        self.assertNotEqual(name, "")
        self.assertNotEqual(name, None)
        self.assertIsInstance(name, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(name, "LUCENT MATTE CROSSBODY BAG")

    def test_product_amount(self):
        amount = self.product.product_amount()

        self.assertNotEqual(amount, "")
        self.assertNotEqual(amount, None)
        self.assertIsInstance(amount, float)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(amount, 565)

    def test_product_currency(self):
        currency = self.product.product_currency()

        self.assertNotEqual(currency, "")
        self.assertNotEqual(currency, None)
        self.assertIsInstance(currency, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(currency, "$")

    def test_product_material(self):
        material = self.product.product_material()

        self.assertNotEqual(material, "")
        self.assertNotEqual(material, None)
        self.assertIsInstance(material, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(
            material,
            "Surface: Vinyl chloride resin / Base cloth: 100% polyester / Lining: 100% nylon / Tape: 100% nylon / Part: Artificial leather",
        )

    def test_product_sku(self):
        sku = self.product.product_sku()

        self.assertNotEqual(sku, "")
        self.assertNotEqual(sku, None)
        self.assertIsInstance(sku, str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(sku, "BB08AG685")

    def test_product_colors(self):
        color = self.product.product_colors()

        self.assertNotEqual(color, [])
        self.assertNotEqual(color, None)
        self.assertIsInstance(color, list)
        self.assertEqual(type(color[0]), str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(color, ["Light Gray", "Gray", "Black"])

    def test_product_images(self):
        images = self.product.product_images()

        self.assertNotEqual(images, [])
        self.assertNotEqual(images, None)
        self.assertIsInstance(images, list)
        self.assertEqual(type(images[0]), str)

    def test_product_dimensions_none(self):
        dimensions = self.product.product_dimensions()

        self.assertNotEqual(dimensions, None)
        self.assertIsInstance(dimensions, str)
        self.assertNotEqual(dimensions, "")
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(dimensions, "Unavailable")

    def test_product_dimensions(self):
        html = BaoBaoHtml.get_html_data(
            self, "https://us-store.isseymiyake.com/products/wring-crossbody-bag"
        )

        product = BaoBaoProductDocument(html)

        dimensions = product.product_dimensions()

        self.assertNotEqual(dimensions, None)
        self.assertIsInstance(dimensions, str)
        self.assertNotEqual(dimensions, "")
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(dimensions, "9.3 in x 9.3 in x 3.1 in")

    def test_product_description(self):
        description = self.product._product_description()

        self.assertNotEqual(description, None)
        self.assertNotEqual(description, "")

    def test_product_description_index_of_type(self):
        string = "Material:"

        index = self.product._index_of_type(self.description, string)

        self.assertNotEqual(index, None)
        self.assertTrue(index >= 0)

    def test_product_description_index_of_type_missing(self):
        text = "Test text that does not have the desired keyword."
        string = "Material:"

        index = self.product._index_of_type(text, string)

        self.assertNotEqual(index, None)
        self.assertEqual(index, -1)

    def test_product_description_paragraph(self):
        paragraph_one = self.product._paragraph(1)
        paragraph_two = self.product._paragraph(2)

        self.assertIsInstance(paragraph_one, str)
        self.assertNotEqual(paragraph_one, "")
        self.assertNotEqual(paragraph_two, paragraph_one)

    def test_find_text_in_description_block(self):
        text = self.product._find_text_in_description_block("Material:")

        self.assertNotEqual(text, None)
        self.assertIsInstance(text, str)
        self.assertNotEqual(text, "")
        self.assertNotEqual(text[10:], "Material:")

    def test_find_text_in_description_block_unavailable(self):
        text = self.product._find_text_in_description_block("Test:")

        self.assertNotEqual(text, None)
        self.assertIsInstance(text, str)
        self.assertNotEqual(text, "")
        self.assertEqual(text, "Unavailable")

    def test_find_index_in_paragraphs(self):
        paragraph = self.product._find_text_in_paragraphs(2, "Material:")
        paragraph_dimensions = self.product._find_text_in_paragraphs(5, "Dimensions:")
        paragraph_test = self.product._find_text_in_paragraphs(3, "Test:")
        paragraph_empty = self.product._find_text_in_paragraphs(3, "")

        self.assertNotEqual(paragraph, None)
        self.assertNotEqual(paragraph, "")
        self.assertIsInstance(paragraph, str)
        self.assertIsInstance(paragraph_dimensions, str)
        self.assertEqual(paragraph_test, "Unavailable")
        self.assertEqual(paragraph_empty, "Unavailable")

    def test_clean_description_type_text(self):
        description = "Material: Polyvinylchloride / Polyester / Nylon Polyurethane Brass Zinc AlloySurface: Vinyl chloride resin / Base cloth: 100% polyester / Lining: 100% nylon / Tape: 100% nylon / Part: Artificial leatherCare: To remove dirt, wipe gently with a damp, tightly wrung soft cloth, and then wipe dry.‚  Do not use paint thinner, benzene, or detergent. To dry, wipe with a soft cloth.Product Code: BB06-AG676Dimensions: 9 x 2.75 x 1in"

        material = self.product._clean_description_type_text(description, "Material:")
        sku = self.product._clean_description_type_text(description, "Product Code:")
        dimensions = self.product._clean_description_type_text(
            description, "Dimensions:"
        )

        self.assertNotEqual(material, None)
        self.assertIsInstance(material, str)
        self.assertNotEqual(material, "")
        self.assertNotEqual(sku, None)
        self.assertIsInstance(sku, str)
        self.assertNotEqual(sku, "")
        self.assertNotEqual(dimensions, None)
        self.assertIsInstance(dimensions, str)
        self.assertNotEqual(dimensions, "")
