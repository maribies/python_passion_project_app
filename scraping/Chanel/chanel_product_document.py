import re
from .chanel_html import ChanelHtml


class ChanelProductDocument:
    def __init__(self, html):
        self.html = html

    def page_title(self):
        page_title = self.html.title.get_text()

        return page_title.rstrip("| CHANEL")

    def product_dimensions(self):
        dimension = self.html.select(".js-dimension")

        return dimension[0].get_text()

    # TODO: Why can't I use this as a helper?
    def product_price(self):
        price = self.html.select(".product-details__price")

        return price[0].get_text(strip=True)

    def product_currency(self):
        try:
            price = self.html.select(".product-details__price")

            text = price[0].get_text(strip=True)

            return re.findall("[^0-9*,. ]", text)[0]

        except IndexError:
            price = self.html.select(".product-details__request")

            text = price[0].get_text(strip=True)

            return text

    def product_amount(self):
        try:
            price = self.html.select(".product-details__price")

            text = price[0].get_text(strip=True)

            amount = "".join(re.findall(r"[\d]", text))

            return float(amount)

        except IndexError:
            return None

    def product_images(self):
        carousel = self.html.select(".product-details__media")

        image_elements = carousel[0].select("img[src]")

        images = []

        for image in image_elements:
            src = image["src"]

            images.append(src)

        return images

    def product_material(self):
        description = self.html.select_one(".product-details__description")

        return description.get_text(strip=True)

    def product_color(self):
        color = self.html.select(".product-details__color")

        return color[0].get_text(strip=True)

    def product_name(self):
        description = self.html.select_one(".product-details__description").get_text(
            strip=True
        )

        title = self.html.select_one(".product-details__title").get_text(strip=True)

        return title + " " + description
