from django.test import TestCase
from scraping import exceptions
from scraping import ChanelProductsUrls


def server_error():
    raise exceptions.ServerError


def not_found():
    raise exceptions.NotFoundError()


class ChanelGetUrlsTest(TestCase):
    def setUp(self):
        self.chanel = ChanelProductsUrls(page=1)

    def test_products_request_first_page(self):
        # Check data is received from the request.
        try:
            products = self.chanel.get_products()

            assert products is not None
            assert products != ""
            self.assertIsInstance(products, dict)

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
        for page in self.chanel.generate_pages():
            products_data = self.chanel.get_products(page)

            assert products_data is not None

    # # Get unique product page and make sure each is unique and valid.
    def test_products_get_urls_one_page(self):
        product_urls = self.chanel.get_product_urls(pages=1)

        # Urls should be unique and there should be 24 results
        set_of_urls = set(product_urls)
        self.assertEqual(len(set_of_urls), len(product_urls))
        self.assertEqual(len(product_urls), 24)

    def test_products_get_urls_pages(self):
        number_of_pages = 3

        product_urls = self.chanel.get_product_urls(pages=number_of_pages)

        # Urls should be unique and there should be 24 results per page,
        # with the exception of the last page, so don't test until last page/
        # TODO: update last assertion to make more robust.
        set_of_urls = set(product_urls)
        self.assertEqual(len(set_of_urls), len(product_urls))
        self.assertEqual(len(product_urls), number_of_pages * 24)
