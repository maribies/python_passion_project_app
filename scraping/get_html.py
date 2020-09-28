import requests
from bs4 import BeautifulSoup
from .exceptions import ServerError, NotFoundError


class GetHTML:
    def __init__(self, url):
        self.url = url

    @classmethod
    def get_response(self, url):
        # Get the response.
        response = requests.get(url)

        # Check the response status and raise exception.
        if response.status_code == 404:
            raise NotFoundError()

        if response.status_code == 500:
            raise ServerError()

        return response

    @classmethod
    def get_request_text(self, response):
        # Return the html to be parsed.
        return response.text

    @classmethod
    def parse_html(self, html_doc):
        # Parse the html document for data structure.
        return BeautifulSoup(html_doc, "html.parser")

    @classmethod
    def get_html_data(self, url):
        response = self.get_response(url)

        html_doc = self.get_request_text(response)

        html_data = self.parse_html(html_doc)

        return html_data
