from scraping.get_html import GetHTML
from scraping.exceptions import ServerError, NotFoundError


class ChanelHtml:
    """A class to get the HTML data for Chanel"""

    def __init__(self, url):
        self.handbags_url = "https://www.chanel.com/us/fashion/handbags/c/1x1x1/"
        self.base_url = "https://www.chanel.com"

    def get_request_text(self, url):
        html_data = GetHTML.get_response(url)

        return html_data.text

    def get_html_data(self, url):
        html_data = GetHTML.get_html_data(url)

        return html_data
