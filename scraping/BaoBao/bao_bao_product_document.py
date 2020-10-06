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
        material = "Unavailable"

        try:
            index_of_material = description.get_text(strip=True).find("Material:")

            if index_of_material > 1:
                material = description.get_text(strip=True)[index_of_material:]

            if material is None or material == "Unavailable":
                try:
                    paragraph = description.select_one("p:nth-of-type(1)")

                except AttributeError:
                    paragraph = description.select_one("p:nth-of-type(2)")

                index_of_material = paragraph.get_text(strip=True).find("Material:")

                if index_of_material > 1:
                    material = paragraph.get_text(strip=True)[index_of_material:]

                else:
                    try:
                        paragraph = description.select_one("p:nth-of-type(3)")

                    except AttributeError:
                        paragraph = description.select_one("p:nth-of-type(4)")

                    material = paragraph.get_text(strip=True)

        except AttributeError:
            material = "N/A"

        index_of_care = material.find("Care:")

        if index_of_care > 1:
            material = material[:index_of_care]

        index_of_dimensions = material.find("Dimensions:")

        if index_of_dimensions > 1:
            material = material[:index_of_dimensions]

        return material.lstrip("Material:")

    def product_sku(self):
        description = self.html.select_one(".product-single__description")
        product_code = "Unavailable"

        try:
            index_of_code = description.get_text(strip=True).find("Product Code:")

            if index_of_code > 1:
                product_code = description.get_text(strip=True)[
                    index_of_code : (index_of_code + 24)
                ]

            if product_code is None or product_code == "Unavailable":
                try:
                    paragraph = description.select_one("p:nth-of-type(2)")

                except AttributeError:
                    try:
                        paragraph = description.select_one("p:nth-of-type(3)")
                    except AttributeError:
                        paragraph = description.select_one("p:nth-of-type(4)")

                index_of_code = paragraph.get_text(strip=True).find("Product Code:")

                if index_of_code > 1:
                    product_code = paragraph.get_text(strip=True)[
                        index_of_code : (index_of_code + 24)
                    ]

        except AttributeError:
            product_code = "N/A"

        index_of_material = product_code.find("Material:")

        if index_of_material > 1:
            product_code = product_code[:index_of_material]

        index_of_care = product_code.find("Care:")

        if index_of_care > 1:
            product_code = product_code[:index_of_care]

        index_of_dimensions = product_code.find("Dimensions:")

        if index_of_dimensions > 1:
            product_code = product_code[:index_of_dimensions]

        # If the product doesn't have an '-', then the M from material is returned
        # in the 24 length from the trimming of the code above.
        # Being "shamlessly green" now, can be improved later.
        if product_code[-1] == "M":
            product_code = product_code[:-1]

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
        dimensions = "Unavailable"

        try:
            index_of_dimensions = description.get_text(strip=True).find("Dimensions:")

            if index_of_dimensions > 1:
                dimensions = description.get_text(strip=True)[index_of_dimensions:]

            if dimensions is None or dimensions == "Unavailable":
                try:
                    paragraph = description.select_one("p:nth-of-type(3)")

                except AttributeError:
                    paragraph = description.select_one("p:nth-of-type(4)")

                index_of_dimensions = paragraph.get_text(strip=True).find("Dimensions:")

                if index_of_dimensions > 1:
                    dimensions = paragraph.get_text(strip=True)[index_of_dimensions:]

        except AttributeError:
            dimensions = "N/A"

        index_of_material = dimensions.find("Material:")

        if index_of_material > 1:
            dimensions = dimensions[:index_of_material]

        return dimensions.lstrip("Dimensions:")
