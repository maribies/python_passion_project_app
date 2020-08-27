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
    ProductQuantity,
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

    designer = Designer(
        name=designer_data["name"], site_url=designer_data["site_url"]
    )

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
        currency=product_price["currency"],
        amount=float(product_price["amount"]),
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


def create_and_save_product_stock(product_data):
    product_stock = product_data["stock"]
    product_color = product_stock["color"]
    product_quantity = product_stock["quantity"]
    name = product_data["name"]

    color = ProductColor(color=product_color)
    color.save()

    quantity = ProductQuantity(quantity=product_quantity)
    quantity.save()

    stock = ProductStock(name=name, colors=color, quantities=quantity)
    stock.save()

    return stock


def create_and_save_product_images(product_data):
    product_images = product_data["images"]
    name = product_data["name"]

    for product_image in product_images:
        image = ProductImage(name=name, image=product_image)
        image.save()

    return image


def create_and_save_product_objects(product_data):
    description = create_product_description(product_data["product_description"])
    price = create_product_price(product_data["product_price"])
    details = create_product_details(product_data["product_details"])

    description.save()
    price.save()
    details.save()

    return {'description': description, 'price': price, 'details': details}


class Command(BaseCommand):
    help = "Scrape for data"

    def handle(self, *args, **options):
        business = create_business()

        business.save()

        self.stdout.write(self.style.SUCCESS("Successfully saved business."))

        designer = create_designer()

        designer.save()

        self.stdout.write(self.style.SUCCESS("Successfully saved designer."))

        products_data = get_products()

        if len(products_data) == 0 or products_data is None:
            raise CommandError("No products data!")

        for product_data in products_data:
            product_objects = create_and_save_product_objects(product_data)

            stock = create_and_save_product_stock(product_data)

            image = create_and_save_product_images(product_data)

            product = Product(
                name=product_data["name"],
                designer=product_data["designer"],
                product_description=product_objects["description"],
                product_price=product_objects["price"],
                site_url=product_data["site_url"],
                stock=stock,
                product_details=product_objects["details"],
                condition=product_data["condition"],
                image=image,
            )

            product.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully scraped and saved product data.")
        )
