from .chanel_product_document import ChanelProductDocument
from .chanel_html import ChanelHtml
import json
import math
import re


class ChanelProductsUrls:
    """A class to get the urls for all Chanel products."""

    def __init__(self, page=1):
        self.url = f"https://www.chanel.com/us/fashion/handbags/c/1x1x1/?requestType=ajax&page={page}&totalElementsCount=24"
        self.data = self.get_products(page=1)
        self.html = ChanelHtml.get_html_data(self, self.url)
        self.document = ChanelProductDocument(self.html)
        self.base_url = "https://www.chanel.com"

    def get_products(self, page=1):
        url = f"https://www.chanel.com/us/fashion/handbags/c/1x1x1/?requestType=ajax&page={page}&totalElementsCount=24"

        products_data = ChanelHtml.get_request_text(self, url)

        data = json.loads(products_data)

        return data

    def check_products_next_page(self, page=1):
        products_data = self.get_products(page)

        return products_data["next"]

    def get_last_page_number(self):
        total_results = self.data["totalResults"]

        total_results_number = "".join(re.findall("[0-9*,]", total_results))

        last_page = math.ceil(int(total_results_number) / 24)

        return last_page

    def generate_pages(self):
        for page in range(self.get_last_page_number() + 1):
            yield page

    def check_last_page(self):
        last_page_number = self.get_last_page_number()

        return self.check_products_next_page(last_page_number)

    def make_complete_url(self, url_path, id):
        modified_url = url_path.replace(id.lower(), id)

        return self.base_url + modified_url

    def get_products_ids(self, data):
        return data.get("dataLayer", {}).get("productList", {}).keys()

    def get_product_urls(self, pages):
        # TODO: Process in chunks in case of failure?
        urls = []

        for page in range(1, pages + 1):
            products_data = self.get_products(page)
            products_ids = self.get_products_ids(products_data)

            for id in products_ids:
                url_path = (
                    products_data.get("dataLayer", {})
                    .get("productList", {})
                    .get(id, {})
                    .get("quickviewPopin", {})
                    .get("page", {})
                )

                url = self.make_complete_url(url_path, id)

                urls.append(url)

        return urls
