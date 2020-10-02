from retail_app.models import (
    Product,
    ProductPrice,
    ProductColor,
    ProductStock,
    ProductImage,
    SearchProductKeywords,
)


class BaoBaoProductBuilder:
    def __init__(self, document, product):
        self.document = document
        self.product = product

    # TODO: Update to sort by series...
    # Kuro, Lucent, Prism, Crispy, Drape, Liner, Hiker, ROW BI-COLOR, Wring
    # From description/name
    def collection(self):
        return "New"

    # TODO: Could see if there is reference to season or updated in the description to be current and if not, it's permanent.
    def season(self):
        return "Current"

    def create_product_price(self):
        return ProductPrice.objects.update_or_create(
            currency=self.document.product_currency(),
            amount=self.document.product_amount(),
        )

    def create_product(self):
        return Product.objects.update_or_create(
            name=self.document.product_name(),
            designer="Issey Miyake",
            product_price=ProductPrice.objects.get(
                amount=self.document.product_amount(),
                currency=self.document.product_currency(),
            ),
            site_url=self.product.get("url"),
            condition="New",
            material=self.document.product_material(),
            size="OS",
            dimensions=self.document.product_dimensions(),
            sku=self.document.product_sku(),
            season=self.season(),
            collection=self.collection(),
            category="Bags",
            brand="Bao Bao",
        )

    def create_product_color(self, color):
        return ProductColor.objects.update_or_create(color=color)

    def create_product_colors(self):
        colors = self.document.product_colors()

        for color in colors:
            return self.create_product_color(color)

    # TODO: Try to figure out if stock numbers can be retrevied from script in html.
    def create_product_stock(self):
        colors = self.document.product_colors()

        for color in colors:
            return ProductStock.objects.update_or_create(
                color=ProductColor.objects.get(color=color),
                product=Product.objects.get(name=self.document.product_name()),
                quantity=None,
            )

    def create_product_image(self):
        images = self.document.product_images()

        product = Product.objects.get(name=self.document.product_name())

        for image in images:
            return ProductImage.objects.update_or_create(
                product=product, image_url=image
            )

    def keywords(self):
        keywords = (
            self.document.product_name()
            + " "
            + self.document.product_material()
            + " "
            + self.collection()
            + " "
            + self.season()
            + " "
            + self.document.product_sku()
            + " "
            + "Bao Bao Issey Miyake"
        )

        keywords += " " + " ".join(self.document.product_colors())

        return keywords

    def create_keywords(self):
        product = Product.objects.get(name=self.document.product_name())

        keywords = self.keywords()

        return SearchProductKeywords.objects.update_or_create(
            product=product, keywords=keywords
        )

    def create_all_product_information(self):
        print("Creating product fields... This will take a minute or so.")

        self.create_product_price()
        self.create_product()
        self.create_product_colors()
        self.create_product_stock()
        self.create_product_image()
        self.create_keywords()
