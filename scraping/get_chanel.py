from . import GetHTML, ProcessHTML
import json
import re
import math


class DesignerChanel:
    handbags_url = "https://www.chanel.com/us/fashion/handbags/c/1x1x1/"
    base_url = "https://www.chanel.com"

    def get_site_data(self, url=handbags_url):
        html_data = GetHTML.get_html_data(url)

        return html_data

    def make_complete_url(self, url_path, id):
        modified_url = url_path.replace(id.lower(), id)

        return self.base_url + modified_url

    def get_products(self, page=1):
        url = f"https://www.chanel.com/us/fashion/handbags/c/1x1x1/?requestType=ajax&page={page}&totalElementsCount=24"
        products_data = GetHTML.make_request(url)

        data = json.loads(products_data)

        return data

    def check_products_next_page(self, page=1):
        products_data = self.get_products(page)

        return products_data["next"]

    # Getting from the scraping of the website here, but could've gotten from the request- "totalResults".
    def get_total_results(self):
        html_data = self.get_site_data()

        total_results = html_data.select(".js-filters-total-results")

        total_results_number = "".join(
            re.findall("[0-9*,]", total_results[0].get_text())
        )

        return int(total_results_number)

    def get_last_page_number(self):
        total_results = self.get_total_results()

        last_page = math.ceil(total_results / 24)

        return last_page

    def check_last_page(self):
        last_page_number = self.get_last_page_number()

        return self.check_products_next_page(last_page_number)

    def generate_pages(self):
        for page in range(self.get_last_page_number() + 1):
            yield page

    # TODO: organize behaviors into a class for pages, urls and url.
    def get_product_urls(self, pages):
        # TODO: Process in chunks in case of failure?
        urls = []

        for page in range(1, pages + 1):
            products_data = self.get_products(page)
            products_ids = (
                products_data.get("dataLayer", {}).get("productList", {}).keys()
            )

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

    def get_product_html(self, url):
        # TODO: need to handle 404 error, etc here?
        html = self.get_site_data(url)

        return ProcessHTML(html)
