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

        assert price is not None
        # self.assertIsInstance(price, ProductPrice)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        # self.assertEqual(price.amount, 6_500)
        # self.assertEqual(price.currency, "$")

    # Given a product document, a Product class is successfully created.
    def test_create_product_from_document(self):
        self.builder.create_product_price()
        product = self.builder.create_product()

        self.assertNotEqual(product, None)
        # self.assertIsInstance(product, Product)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        # self.assertEqual(product.name, "Classic Handbag Lambskin & Gold-Tone Metal")

    # Given a color, a Color class is successfully created.
    def test_create_color(self):
        color = self.builder.create_product_color()

        self.assertNotEqual(color, None)
        # self.assertIsInstance(color, ProductColor)

    def test_product_stock(self):
        self.builder.create_product_color()
        self.builder.create_product_price()
        self.builder.create_product()
        stock = self.builder.create_product_stock()

        self.assertNotEqual(stock, None)
        # self.assertEqual(stock.__str__(), 'Classic Handbag Lambskin & Gold-Tone Metal - Black - None')

    def test_product_image(self):
        self.builder.create_product_price()
        self.builder.create_product()
        image = self.builder.create_product_image()

        self.assertNotEqual(image, None)
        # self.assertIsInstance(image, ProductImage)

    def test_search_product_keywords(self):
        self.builder.create_product_price()
        self.builder.create_product()
        keywords = self.builder.create_keywords()

        self.assertNotEqual(keywords, None)
        # TODO: why does this pass, shouldn't it be a class instance?
        self.assertTrue(type(keywords), "")

    def test_sku(self):
        sku = self.builder.sku()

        self.assertTrue(len(sku) <= 55)


# TODO: Given a url, a Product class is successfully created.
#     def test_create_product_from_url(self, url):
#         product = self.chanel.create_product(url)

# TODO: Given multiple urls, multiple products are created.
#     def test_create_products_from_url(self):
#         urls = self.products.urls
#         products = []

#         for url in urls:
#             product = self.chanel.create_product(url)

#         products.append(product)
