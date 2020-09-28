from django.test import TestCase
from scraping import exceptions, get_html
from scraping.get_html import GetHTML
from bs4 import BeautifulSoup


def not_found():
    raise exceptions.NotFoundError()


def server_error():
    raise exceptions.ServerError()


class GetHTMLTest(TestCase):
    def setUp(self):
        self.url = "https://www.chanel.com/us/fashion/handbags/c/1x1x1/"
        self.product_url = "https://www.chanel.com/us/fashion/p/A01112Y0129594305/classic-handbag-lambskin-gold-tone-metal/"
        self.bad_product_url = "https://www.chanel.com/us/fashion/p/A01112Y"

    # Given a url, a request is made and html is returned.
    def test_get_response(self):
        try:
            response = GetHTML.get_response(self.url)

            assert response is not None
            assert response.text != ""
            assert response.status_code == 200

        except exceptions.ServerError:
            with self.assertRaises(exceptions.ServerError) as context:
                server_error()

                self.assertTrue("error" in str(context.exception))

        except exceptions.NotFoundError:
            with self.assertRaises(exceptions.NotFoundError) as context:
                not_found()

                self.assertTrue("error" in str(context.exception))

    # Given a bad url, a request is made and html is returned.
    def test_get_bad_response(self):
        try:
            GetHTML.get_response(self.bad_product_url)

        except exceptions.NotFoundError:
            with self.assertRaises(exceptions.NotFoundError) as context:
                not_found()

                self.assertTrue("error" in str(context.exception))

    # Given a url, data is parsed and returned.
    def test_get_html_data(self):
        try:
            html = GetHTML.get_html_data(self.url)

            assert html is not None
            assert html != ""
            self.assertIsInstance(html, BeautifulSoup)

        except exceptions.ServerError:
            with self.assertRaises(exceptions.ServerError) as context:
                server_error()

                self.assertTrue("error" in str(context.exception))

    # Given a product url, data for that product is returned.
    def test_get_chanel_product_html(self):
        html = GetHTML.get_html_data(self.product_url)

        assert html is not None
        assert html != ""
        self.assertIsInstance(html, BeautifulSoup)

    # Given a bad product url, an exception is thrown.
    def test_get_chanel_product_html_failure(self):
        try:
            html = GetHTML.get_html_data(self.bad_product_url)

            assert html is not None
            assert html != ""
            self.assertIsInstance(html, Exception)

        except exceptions.NotFoundError:
            with self.assertRaises(exceptions.NotFoundError) as context:
                not_found()

                self.assertTrue("error" in str(context.exception))
