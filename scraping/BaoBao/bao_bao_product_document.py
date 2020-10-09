import re
from .bao_bao_html import BaoBaoHtml


class BaoBaoProductDocument:
    def __init__(self, html):
        self.html = html

    def product_name(self):
        product_title = self.html.select(".product-single__title")

        return product_title[0].get_text(strip=True)

    def _product_price(self):
        product_price = self.html.select(".product__price")

        text = product_price[0].get_text(strip=True) or product_price[1].get_text(
            strip=True
        )

        return text

    def product_amount(self):
        text = self._product_price()

        amount = "".join(re.findall(r"[\d]", text))

        return float(amount)

    def product_currency(self):
        text = self._product_price()

        currency = re.findall("[^0-9*,. ]", text)[0]

        return currency

    def product_colors(self):
        color_fields = self.html.select(
            ".variant-input-wrap > div > input[data-color-name]"
        )

        return [field["value"] for field in color_fields]

    def product_images(self):
        carousel = self.html.select(".product__thumbs")

        image_elements = carousel[0].select("a")

        return [image["href"] for image in image_elements]

    def _product_description(self):
        return self.html.select_one(".product-single__description")

    def _index_of_type(self, text, string):
        return text.find(string)

    def _paragraph(self, position):
        description = self._product_description()

        try:
            paragraph = description.select_one(f"p:nth-of-type({position})").get_text(
                strip=True
            )

        except AttributeError:
            paragraph = "Unavailable"

        return paragraph

    def _find_text_in_description_block(self, description_type_string):
        description = self._product_description()
        description_type = "Unavailable"

        index = self._index_of_type(
            description.get_text(strip=True), description_type_string
        )

        if index > 1:
            description_type = description.get_text(strip=True)[index:]

        return description_type

    def _find_text_in_paragraphs(self, number_of_paragraphs, description_type_string):
        index = 0

        while number_of_paragraphs > 0 and index <= 0:
            paragraph = self._paragraph(number_of_paragraphs)

            index = self._index_of_type(paragraph, description_type_string)

            if index > 1:
                paragraph[index:]
            else:
                paragraph = "Unavailable"

            number_of_paragraphs = number_of_paragraphs - 1

        return paragraph

    def _get_description_type_text(self, description_type_string):
        try:
            description_type_text = self._find_text_in_description_block(
                description_type_string
            )

            # TODO: This doesn't look needed from a sample of products at least for material, but will leave it as a catch.
            if description_type_text is None or description_type_text == "Unavailable":
                description_type_text = self._find_text_in_paragraphs(
                    4, description_type_string
                )

        except AttributeError:
            description_type_text = "N/A"

        return description_type_text

    def _clean_description_type_text(
        self, description_type_text, description_type_string
    ):
        description_types = ["Material:", "Care:", "Dimensions:", "Product Code:"]

        for description in description_types:
            if description == description_type_string:
                description_type_text
            else:
                index = self._index_of_type(description_type_text, description)

                if index > 1:
                    description_type_text = description_type_text[:index]

        text = description_type_text.lstrip(description_type_string)

        return text.strip()

    def product_material(self):
        description_type_string = "Material:"

        description_type_text = self._get_description_type_text(description_type_string)

        return self._clean_description_type_text(
            description_type_text, description_type_string
        )

    def product_sku(self):
        description_type_string = "Product Code:"

        description_type_text = self._get_description_type_text(description_type_string)

        return self._clean_description_type_text(
            description_type_text, description_type_string
        )

    def product_dimensions(self):
        description_type_string = "Dimensions:"

        description_type_text = self._get_description_type_text(description_type_string)

        return self._clean_description_type_text(
            description_type_text, description_type_string
        )
