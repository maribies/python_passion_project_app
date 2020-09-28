from .chanel_product_document import ChanelProductDocument
from .chanel_html import ChanelHtml
import json
import math
import re


class ChanelProducts:
    """A class to get the products for all Chanel handbags."""

    def __init__(self, page=1):
        self.data = self.get_products(page=1)
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

    def check_last_page(self):
        last_page_number = self.get_last_page_number()

        return self.check_products_next_page(last_page_number)

    def generate_pages(self):
        for page in range(self.get_last_page_number() + 1):
            yield page

    def get_all_products(self):
        results = []

        for page in self.generate_pages():
            products_data = self.get_products(page)

            results.append(products_data)

        return results

    def make_complete_url(self, url_path, id):
        modified_url = url_path.replace(id.lower(), id)

        return self.base_url + modified_url

    def get_products_ids(self, data):
        return data.get("dataLayer", {}).get("productList", {}).keys()

    def get_url_path(self, products_data, id):
        return (
            products_data.get("dataLayer", {})
            .get("productList", {})
            .get(id, {})
            .get("quickviewPopin", {})
            .get("page", {})
        )

    def get_collection_season(self, products_data, id):
        return (
            products_data.get("dataLayer", {})
            .get("productList", {})
            .get(id, {})
            .get("quickviewPopin", {})
            .get("ecommerce", {})
            .get("detail", {})
            .get("products", {})[0]
            .get("dimension18", {})
        )

    # TODO: make this work, but then need to further figure out loops and structures.
    def get_product_information(self, products_ids, products_data):
        products = []

        for id in products_ids:
            # TODO: Should do some sort of validation here.
            url_path = self.get_url_path(products_data, id)

            url = self.make_complete_url(url_path, id)

            collection_season = self.get_collection_season(products_data, id)

            product = {"url": url, "collection_season": collection_season, "id": id}

            products.append(product)

        return products

    def get_products_info(self, pages):
        # TODO: Process in chunks in case of failure?
        all_products = []
        for page in range(1, pages + 1):
            products_data = self.get_products(page)
            products_ids = self.get_products_ids(products_data)

            for id in products_ids:
                url_path = self.get_url_path(products_data, id)

                url = self.make_complete_url(url_path, id)

                collection_season = self.get_collection_season(products_data, id)

                product = {"url": url, "collection_season": collection_season, "id": id}

                all_products.append(product)
            # products = self.get_product_information(products_ids, products_data)
        return all_products

    def get_all_products_info(self):
        return self.get_products_info(self.get_last_page_number())
