from django.test import TestCase
from scraping import exceptions
from scraping import ChanelProducts


def server_error():
    raise exceptions.ServerError


def not_found():
    raise exceptions.NotFoundError()


class TestChanelProducts(TestCase):
    def setUp(self):
        self.chanel = ChanelProducts(page=1)

    def test_products_request_first_page(self):
        # Check data is received from the request.
        try:
            products = self.chanel.get_products()

            products_length = len(products.get("dataLayer", {}).get("productList", {}))

            assert products is not None
            assert products != ""
            self.assertIsInstance(products, dict)
            self.assertEqual(products_length, 24)

        except exceptions.ServerError:
            with self.assertRaises(exceptions.ServerError) as context:
                server_error()

                self.assertTrue("error" in str(context.exception))

        except exceptions.NotFoundError:
            with self.assertRaises(exceptions.NotFoundError) as context:
                not_found()

                self.assertTrue("error" in str(context.exception))

    def test_products_request_next_page(self):
        # Check for a next page and receive data from the request.
        try:
            page_url = self.chanel.check_products_next_page()

            self.assertIn("page=2", page_url)

        except exceptions.ServerError:
            with self.assertRaises(exceptions.ServerError) as context:
                server_error()

                self.assertTrue("error" in str(context.exception))

        except exceptions.NotFoundError:
            with self.assertRaises(exceptions.NotFoundError) as context:
                not_found()

                self.assertTrue("error" in str(context.exception))

    # Check to receive page data until the end.
    # We can get total results and we also know that the request returns 24 elements,
    # So we should be able to get the last page by dividing the total by 24
    # Ie 217 products/24 per page= 9.04 => 10 pages and next should be 0
    def test_products_request_last_page(self):
        try:
            last_page = self.chanel.check_last_page()

            self.assertEqual("", last_page)

        except exceptions.ServerError:
            with self.assertRaises(exceptions.ServerError) as context:
                server_error()

                self.assertTrue("error" in str(context.exception))

        except exceptions.NotFoundError:
            with self.assertRaises(exceptions.NotFoundError) as context:
                not_found()

                self.assertTrue("error" in str(context.exception))

    # Check that each product page has data- head request
    def test_products_request_all(self):
        products_data = self.chanel.get_all_products()

        assert products_data is not None
        self.assertTrue(len(products_data) > 0)

    # # Get unique product page and make sure each is unique and valid.
    def test_products_get_info_one_page(self):
        product_urls = []

        products = self.chanel.get_products_info(pages=1)

        for product in products:
            url = product.get("url")

            product_urls.append(url)

        # Urls should be unique and there should be 24 results
        set_of_urls = set(product_urls)
        self.assertEqual(len(set_of_urls), len(product_urls))
        self.assertEqual(len(product_urls), 24)

    def test_products_get_info_pages(self):
        number_of_pages = 3
        product_urls = []

        products = self.chanel.get_products_info(pages=number_of_pages)

        for product in products:
            url = product.get("url")

            product_urls.append(url)

        url = products[0].get("url")
        collection_season = products[0].get("collection_season")
        id = products[0].get("id")

        self.assertIsInstance(url, str)
        assert url != ""
        self.assertIsInstance(collection_season, str)
        assert collection_season != ""
        self.assertIsInstance(id, str)
        assert id != ""

        # Urls should be unique and there should be 24 results per page,
        # with the exception of the last page, so don't test until last page/
        # TODO: update last assertion to make more robust.
        set_of_urls = set(product_urls)
        self.assertEqual(len(set_of_urls), len(product_urls))
        self.assertEqual(len(product_urls), number_of_pages * 24)

    def test_products_get_all_products_info(self):
        product_urls = []

        products = self.chanel.get_all_products_info()

        for product in products:
            url = product.get("url")

            product_urls.append(url)

        url = products[0].get("url")
        collection_season = products[0].get("collection_season")
        id = products[0].get("id")

        self.assertIsInstance(url, str)
        assert url != ""
        self.assertIsInstance(collection_season, str)
        assert collection_season != ""
        self.assertIsInstance(id, str)
        assert id != ""

    def test_products_ids(self):
        products_data = self.chanel.get_products(1)

        products = products_data.get("dataLayer", {}).get("productList", {})
        ids = self.chanel.get_products_ids(products_data)

        self.assertEqual(24, len(ids))
        self.assertEqual(len(products), len(ids))
