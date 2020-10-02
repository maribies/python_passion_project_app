from django.test import TestCase
from scraping import BaoBaoProducts


class TestBaoBaoProducts(TestCase):
    def setUp(self):
        self.site_url = "https://us-store.isseymiyake.com/collections/baobao"
        self.base_url = "https://us-store.isseymiyake.com"

    def test_get_products_urls(self):
        urls = BaoBaoProducts.get_products_urls(self)

        self.assertNotEqual(urls, [])
        self.assertEqual(type(urls[0]), str)
        self.assertTrue(len(urls) > 2)
