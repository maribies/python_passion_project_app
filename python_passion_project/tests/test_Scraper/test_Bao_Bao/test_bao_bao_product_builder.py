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
        self.html = BaoBaoHtml().get_html_data(self.product.get("url"))
        self.document = BaoBaoProductDocument(self.html)
        self.builder = BaoBaoProductBuilder(self.document, self.product)

    # Given a price, a Price class is successfully created.
    def test_create_price(self):
        price = self.builder.create_product_price()

        amount = price[0].amount
        currency = price[0].currency

        self.assertNotEqual(price, None)
        self.assertIsInstance(price[0], ProductPrice)
        self.assertEqual(type(amount), float)
        self.assertEqual(type(currency), str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(str(price[0]), "$565.0")
        self.assertEqual(amount, 565.0)
        self.assertEqual(currency, "$")

    # Given a product document, a Product class is successfully created.
    def test_create_product(self):
        self.builder.create_product_price()
        product = self.builder.create_product()

        product_name = product[0].name

        self.assertNotEqual(product, None)
        self.assertIsInstance(product[0], Product)
        self.assertEqual(type(product_name), str)
        self.assertNotEqual(type(product_name), "")
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(product_name, "LUCENT MATTE CROSSBODY BAG")

    # Given a color, a Color class is successfully created.
    def test_create_colors(self):
        colors = self.builder.create_product_colors()

        first_color = colors[0][0]

        self.assertNotEqual(colors, None)
        self.assertIsInstance(first_color, ProductColor)
        self.assertEqual(type(first_color.color), str)

    def test_product_stock(self):
        self.builder.create_product_colors()
        self.builder.create_product_price()
        self.builder.create_product()
        stock = self.builder.create_product_stock()

        first_stock = stock[0][0]

        self.assertNotEqual(stock, None)
        self.assertIsInstance(first_stock, ProductStock)
        self.assertNotEqual(first_stock.product, None)
        self.assertTrue(first_stock.quantity is None or type(stock[0].quantity) == int)
        self.assertNotEqual(first_stock.color, None)
        self.assertTrue(len(str(first_stock)) > 1)

    def test_product_images(self):
        self.builder.create_product_price()
        self.builder.create_product()
        images = self.builder.create_product_images()

        first_image = images[0][0]
        first_image_url = first_image.image_url

        self.assertNotEqual(images, None)
        self.assertIsInstance(first_image, ProductImage)
        self.assertEqual(type(first_image_url), str)
        self.assertNotEqual(first_image.product, None)
        self.assertTrue(len(first_image_url) > 1)

    def test_search_product_keywords(self):
        self.builder.create_product_price()
        self.builder.create_product()
        keywords = self.builder.create_keywords()

        self.assertNotEqual(keywords, None)
        self.assertIsInstance(keywords[0], SearchProductKeywords)
        self.assertEqual(type(keywords[0].keywords), str)
        self.assertIn(keywords[0].product.name, keywords[0].keywords)
