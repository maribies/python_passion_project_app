from scraping.get_html import GetHTML
from scraping.exceptions import ServerError, NotFoundError


class BaoBaoHtml:
    """A class to get the HTML data for Bao Bao"""

    def get_request_text(self, url):
        html_data = GetHTML.get_response(url)

        return html_data.text

    def get_html_data(self, url):
        html_data = GetHTML.get_html_data(url)

        return html_data
