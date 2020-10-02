import re
from .bao_bao_html import BaoBaoHtml


class BaoBaoProductDocument:
    def __init__(self, html):
        self.html = html

    def product_name(self):
        product_title = self.html.select(".product-single__title")

        return product_title[0].get_text(strip=True)

    def product_price(self):
        product_price = self.html.select(".product__price")

        return product_price[0].get_text(strip=True)

    def product_amount(self):
        price = self.html.select(".product__price")

        text = price[0].get_text(strip=True)

        amount = "".join(re.findall(r"[\d]", text))

        return float(amount)

    def product_currency(self):
        price = self.html.select(".product__price")

        text = price[0].get_text(strip=True)

        return re.findall("[^0-9*,. ]", text)[0]

    def product_material(self):
        description = self.html.select_one(".product-single__description")

        if len(description.select("p")) == 6:
            return description.select_one("p:nth-of-type(5)").get_text(strip=True)

        try:
            material = (
                description.select_one("p:nth-of-type(4)")
                .get_text(strip=True)
                .lstrip("Material:")
            )

        except AttributeError:
            material = (
                description.select_one("p:nth-of-type(3)")
                .get_text(strip=True)
                .lstrip("Material:")
            )

        return material

    def product_sku(self):
        description = self.html.select_one(".product-single__description")

        index_of_code = (
            description.select_one("p:nth-of-type(2)")
            .get_text(strip=True)
            .find("Product Code:")
        )

        if index_of_code == -1:
            product_code = description.select_one("p:nth-of-type(3)").get_text(
                strip=True
            )

        else:
            product_code = description.select_one("p:nth-of-type(2)").get_text(
                strip=True
            )[index_of_code:]

        return product_code.lstrip("Product Code:")

    def product_colors(self):
        color_fields = self.html.select(
            ".variant-input-wrap > div > input[data-color-name]"
        )

        colors = []

        for field in color_fields:
            color = field["value"]

            colors.append(color)

        return colors

    def product_images(self):
        carousel = self.html.select(".product__thumbs")

        image_elements = carousel[0].select("a")

        images = []

        for image in image_elements:
            src = image["href"]

            images.append(src)

        return images

    def product_dimensions(self):
        description = self.html.select_one(".product-single__description")

        if len(description.select("p")) == 5:
            return "N/A"

        else:
            try:
                dimensions = description.select_one("p:nth-of-type(4)").get_text(
                    strip=True
                )

                return dimensions.lstrip("Dimensions:")

            except AttributeError:
                return "N/A"
