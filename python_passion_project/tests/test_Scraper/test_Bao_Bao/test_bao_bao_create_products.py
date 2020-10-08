from django.test import TestCase
from scraping import BaoBao


class TestGetBaoBaoProducts(TestCase):
    def setUp(self):
        self.product_url = [
            "https://us-store.isseymiyake.com/collections/baobao/products/prism-frost-tote-bag"
        ]
        self.products_urls = [
            "https://us-store.isseymiyake.com/collections/baobao/products/prism-frost-tote-bag",
            "https://us-store.isseymiyake.com/collections/baobao/products/prism-frost-crossbody-bag",
            "https://us-store.isseymiyake.com/collections/baobao/products/prism-frost-pouch",
            "https://us-store.isseymiyake.com/collections/baobao/products/drape-tote-bag",
            "https://us-store.isseymiyake.com/collections/baobao/products/wring-nubuck-crossbody-bag",
        ]

    # Given [urls], creates products.
    def test_create_product(self):
        products = BaoBao().create_products(self.product_url)

        self.assertNotEqual(products, None)
        self.assertEqual(products, 1)

    def test_create_products(self):
        products = BaoBao().create_products(self.products_urls)

        self.assertNotEqual(products, None)
        self.assertEqual(products, len(self.products_urls))

    # TODO: See if it's possible to refactor/test to continue to create products
    # and just skip over bad urls... but not sure with exception being nested all the way
    # back to getHTML.
