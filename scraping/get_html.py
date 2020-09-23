import requests
from bs4 import BeautifulSoup


class GetHTML:
    def __init__(self, url):
        self.url = url

    @classmethod
    def make_request(self, url):
        # Get the HTML of the website
        r = requests.get(url)

        # Return the html to be parsed.
        return r.text

    @classmethod
    def parse_html(self, html_doc):
        # Parse the html document for data structure.
        return BeautifulSoup(html_doc, "html.parser")

    @classmethod
    def get_html_data(self, url):
        html_doc = self.make_request(url)

        html_data = self.parse_html(html_doc)

        return html_data
