from . import get_html
import json
import re
import math


def get_site_data():
    html_data = get_html.get_html_data("https://www.chanel.com/us/fashion/handbags/c/1x1x1/")

    return html_data


def get_ajax_request(page=1):
    ajax_data = get_html.make_request(f"https://www.chanel.com/us/fashion/handbags/c/1x1x1/?requestType=ajax&page={page}&totalElementsCount=24")

    return ajax_data


def check_ajax_next_page(page=1):
    ajax_data = get_ajax_request(page)

    data = json.loads(ajax_data)

    return data["next"]


# Getting from the scraping of the website here, but could've gotten from the ajax request- "totalResults".
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

    return check_ajax_next_page(last_page_number)
