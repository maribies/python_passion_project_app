from django.test import TestCase
from scraping import (
    BaoBaoHtml,
    BaoBaoProductBuilder,
    BaoBaoProductDocument,
    BaoBaoProducts,
)
from retail_app.models import (
    Product,
    ProductColor,
    ProductImage,
    ProductPrice,
    ProductStock,
    SearchProductKeywords,
)


class TestBaoBaoProductBuilder(TestCase):
    def setUp(self):
        self.product = {
            "url": "https://us-store.isseymiyake.com/collections/baobao/products/lucent-matte-crossbody-bag?variant=32170657579102"
        }
        self.products = BaoBaoProducts()
        self.html = BaoBaoHtml.get_html_data(self, self.product.get("url"))
        self.document = BaoBaoProductDocument(self.html)
        self.builder = BaoBaoProductBuilder(self.document, self.product)

    # Given a price, a Price class is successfully created.
    def test_create_price(self):
        price = self.builder.create_product_price()

        self.assertNotEqual(price, None)
        self.assertIsInstance(price[0], ProductPrice)
        self.assertEqual(type(price[0].amount), float)
        self.assertEqual(type(price[0].currency), str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(price[0].__str__(), "$565.0")
        self.assertEqual(price[0].amount, 565.0)
        self.assertEqual(price[0].currency, "$")

    # Given a product document, a Product class is successfully created.
    def test_create_product(self):
        self.builder.create_product_price()
        product = self.builder.create_product()

        self.assertNotEqual(product, None)
        self.assertIsInstance(product[0], Product)
        self.assertEqual(type(product[0].name), str)
        self.assertNotEqual(type(product[0].name), "")
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(product[0].name, "LUCENT MATTE CROSSBODY BAG")

    # Given a color, a Color class is successfully created.
    def test_create_colors(self):
        colors = self.builder.create_product_colors()

        self.assertNotEqual(colors, None)
        self.assertIsInstance(colors[0][0], ProductColor)
        self.assertEqual(type(colors[0][0].color), str)

    def test_product_stock(self):
        self.builder.create_product_colors()
        self.builder.create_product_price()
        self.builder.create_product()
        stock = self.builder.create_product_stock()

        self.assertNotEqual(stock, None)
        self.assertIsInstance(stock[0][0], ProductStock)
        self.assertNotEqual(stock[0][0].product, None)
        self.assertTrue(stock[0][0].quantity is None or type(stock[0].quantity) == int)
        self.assertNotEqual(stock[0][0].color, None)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(
            stock[0][0].__str__(),
            "LUCENT MATTE CROSSBODY BAG - Light Gray - None",
        )

    def test_product_images(self):
        self.builder.create_product_price()
        self.builder.create_product()
        images = self.builder.create_product_images()

        self.assertNotEqual(images, None)
        self.assertIsInstance(images[0][0], ProductImage)
        self.assertEqual(type(images[0][0].image_url), str)
        self.assertNotEqual(images[0][0].product, None)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(
            images[0][0].image_url,
            "//cdn.shopify.com/s/files/1/0274/9988/8734/products/BB08AG685-11-01_1800x1800.jpg?v=1599862324",
        )

    def test_search_product_keywords(self):
        self.builder.create_product_price()
        self.builder.create_product()
        keywords = self.builder.create_keywords()

        self.assertNotEqual(keywords, None)
        self.assertIsInstance(keywords[0], SearchProductKeywords)
        self.assertEqual(type(keywords[0].keywords), str)
        self.assertIn(keywords[0].product.name, keywords[0].keywords)
