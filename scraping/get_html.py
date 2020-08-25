import requests
from bs4 import BeautifulSoup


def make_request(url):
    # Get the HTML of the website
    r = requests.get(url)

    # Return the html to be parsed.
    return r.text


def parse_html(html_doc):
    # Parse the html document for data structure.
    return BeautifulSoup(html_doc, "html.parser")


def main(url):
    html_doc = make_request(url)

    html_data = parse_html(html_doc)

    return html_data
