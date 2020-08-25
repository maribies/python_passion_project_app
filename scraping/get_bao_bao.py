from . import get_html
import re

url = "https://www.shopbaobaoisseymiyake.com/"
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


def get_product_description(product_html_data):
    product_title = product_html_data.select("#single-product-title")

    product_title_text = product_title[0].get_text()

    # TODO: Determine how want to classify season and collection
    # (and if all categories should be handbag (vs accessory)).
    product_description = {
        "name": product_title_text,
        "season": "N/A",
        "collection": "N/A",
        "category": "Bags",
        "brand": "Bao Bao",
    }

    return product_description


def get_product(product_url):
    product = {}

    # Add product site url & designer to dictonary.
    product["site_url"] = product_url
    product["designer"] = "Issey Miyake"

    # Get data structure for product.
    product_html_data = get_html.main(product_url)

    # TODO: Refactor all other data groups similar to this.
    # Get data for product description & add to product dictonary.
    product["product_description"] = get_product_description(product_html_data)

    def get_product_price(id):
        return id and re.compile("single-product-price").search(id)

    product_price = product_html_data.find(id=get_product_price)

    product_price_text = product_price.get_text()

    product_currency = re.findall("[^0-9*,. ]", product_price_text)
    product_price_amount = re.findall("[0-9*. ]", product_price_text)

    # Add product price to product dictonary.
    product["product_price"] = {
        "currency": "".join(product_currency),
        "amount": "".join(product_price_amount),
    }

    def get_product_colors():
        return product_html_data.select(".single-product-colors")

    product_colors = get_product_colors()

    product_colors_text = []
    product_colors_availability = []

    stock = product_colors[0].select(".single-product-color-title")

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

    # Add product stock to product dictonary.
    product["stock"] = {
        "colors": product_colors_text,
        "quantities": product_colors_availability,
    }

    # Retreive description details.
    def get_product_details():
        return product_html_data.select(".baobao-module-accordion")

    product_details_structure = get_product_details()

    product_details = product_details_structure[0].select(
        ".baobao-module-accordion-content"
    )

    product_details_text = []

    for index, detail_item in enumerate(product_details):
        text = product_details[index].get_text()

        product_details_text.append(text)

    # Add product stock to product dictonary.
    product["product_details"] = {
        "material": product_details_text[2],
        "size": "OS",
        "dimensions": product_details_text[1],
        "sku": "N/A",
    }

    def get_product_image():
        return product_html_data.select(".single-product-image-container")

    product_image_structure = get_product_image()

    product_images = product_image_structure[0].select(".single-product-image")

    product_images_srcs = []

    for index, image_item in enumerate(product_images):
        src = image_item["src"]

        product_images_srcs.append(src)

    # Add product image src to product dictonary.
    product["images"] = product_images_srcs

    # Add product condition to prodcut dictonary.
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
