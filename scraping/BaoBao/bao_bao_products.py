from .bao_bao_html import BaoBaoHtml
import json
import math
import re


class BaoBaoProducts:
    """A class to get the products for all Bao Bao."""

    def __init__(self):
        self.site_url = "https://us-store.isseymiyake.com/collections/baobao"
        self.base_url = "https://us-store.isseymiyake.com"

    def get_products_urls(self):
        products_urls = []

        html = BaoBaoHtml.get_html_data(self, self.site_url)

        links = html.select(".grid-product__link")

        for link in links:
            path = link.get("href")

            product = self.base_url + path

            products_urls.append(product)

        return products_urls
