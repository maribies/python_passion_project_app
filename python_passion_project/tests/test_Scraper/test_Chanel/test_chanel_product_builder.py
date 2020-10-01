from django.test import TestCase
from scraping import (
    ChanelHtml,
    ChanelProductDocument,
    ChanelProducts,
    ChanelProductBuilder,
)
from retail_app.models import (
    Product,
    ProductPrice,
    ProductColor,
    ProductImage,
    ProductStock,
    SearchProductKeywords,
)


class TestChanelProductBuilder(TestCase):
    def setUp(self):
        self.product = {
            "url": "https://www.chanel.com/us/fashion/p/A01112Y0129594305/classic-handbag-lambskin-gold-tone-metal",
            "id": "A01112Y0129594305",
            "collection_season": "reorders",
        }
        self.products = ChanelProducts(page=1)
        self.html = ChanelHtml.get_html_data(self, self.product.get("url"))
        self.document = ChanelProductDocument(self.html)
        self.builder = ChanelProductBuilder(self.document, self.product)

    def test_collection_season(self):
        collection = ChanelProductBuilder.collection(self)
        season = ChanelProductBuilder.season(self)

        self.assertIsInstance(collection, str)
        self.assertIsInstance(season, str)
        self.assertNotEqual(collection, "")
        self.assertNotEqual(season, "")
        self.assertNotEqual(collection, "reorders")
        self.assertNotEqual(season, "reorders")

    # Given a price, a Price class is successfully created.
    def test_create_price(self):
        price = self.builder.create_product_price()

        self.assertNotEqual(price, None)
        self.assertIsInstance(price[0], ProductPrice)
        self.assertEqual(type(price[0].amount), float)
        self.assertEqual(type(price[0].currency), str)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(price[0].__str__(), "$6500.0")
        self.assertEqual(price[0].amount, 6500.0)
        self.assertEqual(price[0].currency, "$")

    # Given a product document, a Product class is successfully created.
    def test_create_product_from_document(self):
        self.builder.create_product_price()
        product = self.builder.create_product()

        self.assertNotEqual(product, None)
        self.assertIsInstance(product[0], Product)
        self.assertEqual(type(product[0].name), str)
        self.assertNotEqual(type(product[0].name), "")
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(product[0].name, "Classic Handbag Lambskin & Gold-Tone Metal")

    # Given a color, a Color class is successfully created.
    def test_create_color(self):
        color = self.builder.create_product_color()

        self.assertNotEqual(color, None)
        self.assertIsInstance(color[0], ProductColor)
        self.assertEqual(type(color[0].color), str)

    def test_product_stock(self):
        self.builder.create_product_color()
        self.builder.create_product_price()
        self.builder.create_product()
        stock = self.builder.create_product_stock()

        self.assertNotEqual(stock, None)
        self.assertIsInstance(stock[0], ProductStock)
        self.assertNotEqual(stock[0].product, None)
        self.assertTrue(stock[0].quantity is None or type(stock[0].quantity) == int)
        self.assertNotEqual(stock[0].color, None)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(
            stock[0].__str__(),
            "Classic Handbag Lambskin & Gold-Tone Metal - Black - None",
        )

    def test_product_image(self):
        self.builder.create_product_price()
        self.builder.create_product()
        image = self.builder.create_product_image()

        self.assertNotEqual(image, None)
        self.assertIsInstance(image[0], ProductImage)
        self.assertEqual(type(image[0].image_url), str)
        self.assertNotEqual(image[0].product, None)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(
            image[0].image_url,
            "https://www.chanel.com/images/t_fashionzoom1/f_jpg/classic-handbag-black-lambskin-gold-tone-metal-lambskin-gold-tone-metal-packshot-default-a01112y0129594305-8818021072926.jpg",
        )

    def test_search_product_keywords(self):
        self.builder.create_product_price()
        self.builder.create_product()
        keywords = self.builder.create_keywords()

        print(keywords, type(keywords))
        self.assertNotEqual(keywords, None)
        self.assertIsInstance(keywords[0], SearchProductKeywords)
        self.assertEqual(type(keywords[0].keywords), str)
        self.assertIn(keywords[0].product.name, keywords[0].keywords)

    def test_sku(self):
        sku = self.builder.sku()

        self.assertTrue(len(sku) <= 55)
