from django.core.management.base import BaseCommand, CommandError
from retail_app.models import (
    Business,
    BusinessDesigner,
    Category,
    Designer,
    Product,
    ProductDescription,
    ProductPrice,
    ProductStock,
    ProductDetails,
    ProductImage,
    ProductColor,
    SearchProductKeywords,
)

import sys

sys.path.append("../scraping")

from scraping import get_bao_bao, get_business, get_designer

# TODO: Turn inputs into prompts from terminal.
# For now, will ask for both business and designer to make it easier.
# In future add a flag for all to get and update all designers by business.
# Use similar logic for a command to update the data,
# as saving creates new instances.
input1 = "Bao Bao"
input2 = "Issey Miyake"


def get_products():
    # TODO: Return file name for scraping site in same format so can select
    # dynamically.
    if input1 == "Bao Bao":
        return get_bao_bao.main()


# TODO: consider moving the creates to separate programs(?)
# so the logic can be used for both creation/saving new
# and also for checking/updating existing?
def create_business():
    business_data = get_business.main(input1)

    for designer in business_data["designers"]:
        business_designer = BusinessDesigner(name=designer)

        business_designer.save()

    for category in business_data["categories"]:
        category = Category(name=category)

        category.save()

    business = Business(
        name=business_data["name"],
        site_url=business_data["site_url"],
        designer=business_designer,
        category=category,
    )

    return business


def create_designer():
    business_data = get_business.main(input1)
    designer_data = get_designer.main(business_data, input2)

    designer = Designer(name=designer_data["name"], site_url=designer_data["site_url"])

    return designer


def create_product_description(product_description):
    description = ProductDescription(
        name=product_description["name"],
        season=product_description["season"],
        collection=product_description["collection"],
        category=product_description["category"],
        brand=product_description["brand"],
    )

    return description


def create_product_price(product_price):
    price = ProductPrice(
        currency=product_price["currency"], amount=float(product_price["amount"]),
    )

    return price


def create_product_details(product_details):
    details = ProductDetails(
        material=product_details["material"],
        size=product_details["size"],
        dimensions=product_details["dimensions"],
        sku=product_details["sku"],
    )

    return details


def create_and_save_product_stock(product_data, product):
    product_stock = product_data["stock"]

    product_colors = product_stock["colors"]
    product_quantities = product_stock["quantities"]
    colors = []

    for index, product_color in enumerate(product_colors):
        color = ProductColor(color=product_color)
        color.save()
        colors.append(color)

        stock = ProductStock(
            color=color, product=product, quantity=product_quantities[index]
        )
        stock.save()

    return stock


def create_and_save_product_images(product_data, product):
    product_images = product_data["images"]
    images = []

    for product_image in product_images:
        image = ProductImage(product=product, image_url=product_image)
        image.save()

    return images


def create_and_save_product_objects(product_data):
    description = create_product_description(product_data["product_description"])
    price = create_product_price(product_data["product_price"])
    details = create_product_details(product_data["product_details"])

    description.save()
    price.save()
    details.save()

    return {"description": description, "price": price, "details": details}


class Command(BaseCommand):
    help = "Scrape for data. --all saves business, designer, and products. To only opt for only one, run just the object to create and save ie --products"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--all", action="store_true", help="Scrape and save all data",
        )

        parser.add_argument(
            "--products",
            action="store_true",
            help="Scrape and save only products data",
        )

        parser.add_argument(
            "--business",
            action="store_true",
            help="Scrape and save only business data",
        )

        parser.add_argument(
            "--designer",
            action="store_true",
            help="Scrape and save only designer data",
        )

    def handle(self, *args, **options):
        if options["business"] or options["all"]:
            business = create_business()

            business.save()

            self.stdout.write(self.style.SUCCESS("Successfully saved business."))

        if options["designer"] or options["all"]:
            designer = create_designer()

            designer.save()

            self.stdout.write(self.style.SUCCESS("Successfully saved designer."))

        if options["products"] or options["all"]:
            products_data = get_products()

            if len(products_data) == 0 or products_data is None:
                raise CommandError("No products data!")

            for product_data in products_data:
                product_objects = create_and_save_product_objects(product_data)

                product = Product(
                    name=product_data["name"],
                    designer=product_data["designer"],
                    product_description=product_objects["description"],
                    product_price=product_objects["price"],
                    site_url=product_data["site_url"],
                    product_details=product_objects["details"],
                    condition=product_data["condition"],
                )

                product.save()

                create_and_save_product_stock(product_data, product)

                create_and_save_product_images(product_data, product)

                SearchProductKeywords.create_keywords(product_data, product)

            self.stdout.write(
                self.style.SUCCESS("Successfully scraped and saved product data.")
            )
