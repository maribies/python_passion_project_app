from . import get_html, AbstractUrl, ProcessHTML
import json
import re
import math


def get_site_data(url="https://www.chanel.com/us/fashion/handbags/c/1x1x1/"):
    html_data = get_html.get_html_data(url)

    return html_data


def get_products(page=1):
    products_data = get_html.make_request(
        f"https://www.chanel.com/us/fashion/handbags/c/1x1x1/?requestType=ajax&page={page}&totalElementsCount=24"
    )

    data = json.loads(products_data)

    return data


def check_products_next_page(page=1):
    products_data = get_products(page)

    return products_data["next"]


# Getting from the scraping of the website here, but could've gotten from the request- "totalResults".
def get_total_results():
    html_data = get_site_data()

    total_results = html_data.select(".js-filters-total-results")

    total_results_number = "".join(re.findall("[0-9*,]", total_results[0].get_text()))

    return int(total_results_number)


def get_last_page_number():
    total_results = get_total_results()

    last_page = math.ceil(total_results / 24)

    return last_page


def check_last_page():
    last_page_number = get_last_page_number()

    return check_products_next_page(last_page_number)


def generate_pages():
    for page in range(get_last_page_number() + 1):
        yield page


# TODO: organize behaviors into a class for pages, urls and url.
def get_product_urls(pages):
    # TODO: Process in chunks in case of failure?
    urls = []

    for page in range(1, pages + 1):
        products_data = get_products(page)
        products_ids = products_data.get("dataLayer", {}).get("productList", {}).keys()

        for id in products_ids:
            url_path = (
                products_data.get("dataLayer", {})
                .get("productList", {})
                .get(id, {})
                .get("quickviewPopin", {})
                .get("page", {})
            )

            url = AbstractUrl(url_path)

            url.url_path = url.make_chanel_complete_url(id)

            urls.append(url)

    return urls


def get_product_html(url):
    # TODO: need to handle 404 error, etc here?
    html = get_site_data(url)

    return ProcessHTML(html)
