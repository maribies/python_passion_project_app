from .chanel_html import ChanelHtml
from .chanel_products import ChanelProducts
from .chanel_product_document import ChanelProductDocument
from retail_app.models import (
    Product,
    ProductPrice,
    ProductColor,
    ProductStock,
    ProductImage,
    SearchProductKeywords,
)


class ChanelProductBuilder:
    def __init__(self, document, product):
        self.document = document
        self.product = product

    # TODO: Update to sort new, classic, 2.55, 19, Gabrielle, & Boy
    # Should be able to get from product name.
    def collection(self):
        info = self.product.get("collection_season").split()

        if info[0] == "reorders":
            return "Permanent"

        return info[0]

    def season(self):
        info = self.product.get("collection_season").split()

        if info[0] == "reorders":
            return "Permanent"

        return info[1]

    def sku(self):
        return self.product.get("id")

    def create_product_price(self):
        return ProductPrice.objects.update_or_create(
            currency=self.document.product_currency(),
            amount=self.document.product_amount(),
        )

    # TODO: create methods for sku and url to check/verify/handle failures.
    # Chanel is a little different in that urls are different for color vairants,
    # unlike Bao Bao and original model.
    # Will need to allow for multiple skus, urls under name, and then use
    # a combo of name, price, and dimensions to make sure stock/colors and images are properly grouped.
    def create_product(self):
        return Product.objects.update_or_create(
            name=self.document.product_name(),
            designer="Chanel",
            product_price=ProductPrice.objects.get(
                amount=self.document.product_amount(),
                currency=self.document.product_currency(),
            ),
            site_url=self.product.get("url"),
            condition="New",
            material=self.document.product_material(),
            size="OS",
            dimensions=self.document.product_dimensions(),
            sku=self.sku(),
            season=self.season(),
            collection=self.collection(),
            category="Bags",
            brand="Chanel",
        )

    def create_product_color(self):
        return ProductColor.objects.update_or_create(
            color=self.document.product_color()
        )

    def create_product_stock(self):
        product = Product.objects.get(site_url=self.product.get("url"))

        return ProductStock.objects.update_or_create(
            color=ProductColor.objects.get(color=self.document.product_color()),
            product=product,
            quantity=None,
        )

    def create_product_image(self):
        images = self.document.product_images()

        product = Product.objects.get(site_url=self.product.get("url"))

        for image in images:
            return ProductImage.objects.update_or_create(
                product=product, image_url=image
            )

    def keywords(self):
        return (
            self.document.product_name()
            + " "
            + self.document.product_color()
            + " "
            + self.document.product_material()
            + " "
            + self.collection()
            + " "
            + self.season()
            + " "
            + self.sku()
            + " "
            + "Chanel"
        )

    def create_keywords(self):
        product = Product.objects.get(site_url=self.product.get("url"))

        keywords = self.keywords()

        return SearchProductKeywords.objects.update_or_create(
            product=product, keywords=keywords
        )

    def create_all_product_information(self):
        print("Creating product fields... This will take a minute or so.")

        self.create_product_price()
        self.create_product()
        self.create_product_color()
        self.create_product_stock()
        self.create_product_image()
        self.create_keywords()
