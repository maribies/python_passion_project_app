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
        assert collection != ""
        assert season != ""
        assert collection != "reorders"
        assert season != "reorders"

    # Given a price, a Price class is successfully created.
    def test_create_price(self):
        price = self.builder.create_product_price()

        assert price is not None
        self.assertIsInstance(price, ProductPrice)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(price.amount, 6_500)
        self.assertEqual(price.currency, "$")

    # Given a product document, a Product class is successfully created.
    def test_create_product_from_document(self):
        product = self.builder.create_product()

        assert product is not None
        self.assertIsInstance(product, Product)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        self.assertEqual(product.name, "Classic Handbag Lambskin & Gold-Tone Metal")

    # Given a color, a Color class is successfully created.
    def test_create_color(self):
        color = self.builder.create_product_color()

        assert color is not None
        self.assertIsInstance(color, ProductColor)
        # TODO: This is obviously very specific based on the static url given above, and both should be generic.
        # Also, color is a product instance and need to check value.
        # self.assertEqual(color, 'Black')

    def test_product_stock(self):
        stock = self.builder.create_product_stock()

        assert stock is not None
        self.assertIsInstance(stock, ProductStock)
        self.assertIsInstance(stock.color, ProductColor)

    def test_product_image(self):
        image = self.builder.create_product_image()

        assert image is not None
        self.assertIsInstance(image, ProductImage)


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
