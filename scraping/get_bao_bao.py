from . import get_html
import re

url = "https://www.shopbaobaoisseymiyake.com/shop-all"
products = []


# Produces a collection of all product urls.
def get_products_urls(html_data):
    # The index for the prodcut urls.
    product_urls = []

    # Filters the html data structure to return only product data.
    products = html_data.select("div[data-product-id], div[data-product-url]")

    # Loop through each product structure to return the prodcut url.
    for product in products:
        url = product.get("data-product-url")

        product_urls.append(url)

    return product_urls


def get_product_name(product_html_data):
    product_title = product_html_data.select("#single-product-title")

    product_title_text = product_title[0].get_text()

    return product_title_text


def get_product_description(product_html_data):
    name = get_product_name(product_html_data)

    # TODO: Determine how want to classify season and collection
    # (and if all categories should be handbag (vs accessory)).
    product_description = {
        "name": name,
        "season": "N/A",
        "collection": "N/A",
        "category": "Bags",
        "brand": "Bao Bao",
    }

    return product_description


def get_clean_color_and_quantity(colors, stock):
    product_colors_text, product_colors_availability = [], []

    for index, stock_item in enumerate(stock):
        text = stock[index].get_text()

        color = re.search("(.*)(?=[0-9])", text)
        quantity = re.search("[0-9](.*)", text)

        if color is not None and quantity is not None:
            color_text = color.group(0)
            quantity_text = quantity.group(0)

            hasNumberInColor = re.search(r"[^\d]*[\d]+[^\d]+([\d]+)", quantity_text)

            if hasNumberInColor:
                quantity_text = hasNumberInColor.group(1)

        if color is None:
            color_text = text
            quantity_text = ""

        quantity_number = "".join(re.findall("[0-9*,. ]", quantity_text))
        if quantity_number == "":
            number = None
        else:
            number = quantity_number.strip()

        product_colors_text.append(color_text.strip())
        product_colors_availability.append(number)

    stock = {"colors": product_colors_text, "quantities": product_colors_availability}

    return stock


def get_product_color_and_quantity(product_html_data):
    colors = product_html_data.select(".single-product-colors")

    all_stock = colors[0].select(".single-product-color-title")

    return get_clean_color_and_quantity(colors, all_stock)


def get_product_stock(product_html_data):
    stock = get_product_color_and_quantity(product_html_data)

    return stock


def get_product_price(product_html_data):
    product_price = product_html_data.select("#single-product-price")
    product_price_text = product_price[0].get_text()

    product_currency = re.findall("[^0-9*,. ]", product_price_text)
    product_price_amount = re.findall("[0-9*. ]", product_price_text)

    # Add product price to product dictonary.
    price = {
        "currency": "".join(product_currency),
        "amount": "".join(product_price_amount),
    }

    return price


def get_color_sku(product_html_data):
    colors = product_html_data.select(".single-product-colors")
    color_active = colors[0].select(".active")

    # This formating gives sku with color info.
    sku = color_active[0].get("data-product-sku")

    return sku


def get_product_sku(product_html_data):
    raw_sku = get_color_sku(product_html_data)

    # This formating removes the color details from the sku.
    sku = re.split(r"[-]\d+", raw_sku)

    if len(sku) > 12:
        sku = sku[0:12]

    return sku[0]


def get_product_details(product_html_data):
    sku = get_product_sku(product_html_data)

    product_details_structure = product_html_data.select(".baobao-module-accordion")

    product_details = product_details_structure[0].select(
        ".baobao-module-accordion-content"
    )

    product_details_text = []

    for index, detail_item in enumerate(product_details):
        text = product_details[index].get_text()

        product_details_text.append(text)

    details = {
        "material": product_details_text[2],
        "size": "OS",
        "dimensions": product_details_text[1],
        "sku": sku,
    }

    return details


def get_product_images(product_html_data):
    product_image_structure = product_html_data.select(
        ".single-product-image-container"
    )

    product_images = product_image_structure[0].select(".single-product-image")

    product_images_srcs = []

    for index, image_item in enumerate(product_images):
        src = image_item["src"]

        product_images_srcs.append(src)

    return product_images_srcs


def get_product(product_url):
    product = {}

    # Add product site url & designer to dictonary.
    product["site_url"] = product_url
    product["designer"] = "Issey Miyake"

    # Get data structure for product.
    product_html_data = get_html.main(product_url)

    # Get data for each field & add to product dictonary.
    product["product_description"] = get_product_description(product_html_data)
    product["name"] = get_product_name(product_html_data)
    product["stock"] = get_product_stock(product_html_data)
    product["product_price"] = get_product_price(product_html_data)
    product["product_details"] = get_product_details(product_html_data)
    product["images"] = get_product_images(product_html_data)

    # Add product condition to product dictonary.
    product["condition"] = "New"

    return product


# Loop through product urls list and get data after urls are present.
def get_products(product_urls):
    print("Getting products... This will take a minute or so.")

    for product_url in product_urls:
        product = get_product(product_url)

        products.append(product)

    return products


def main():
    # Get the html data.
    html_data = get_html.main(url)

    print("HTML data successfully scraped.")

    product_urls_index = get_products_urls(html_data)

    print("Product urls successfully indexed.")

    products = get_products(product_urls_index)

    print("Products listed.")

    return products
