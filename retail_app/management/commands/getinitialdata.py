from django.core.management.base import BaseCommand, CommandError
from retail_app.models import Business, Business_Designer, Category, Designer, Product, Product_Description, Product_Price, Product_Stock, Product_Details, Product_Image, Product_Color, Product_Quantity

import re
import sys
sys.path.append('../scraping')

from scraping import get_bao_bao, get_business, get_designer

#TODO: Turn inputs into prompts from terminal.
#### For now, will ask for both business and designer to make it easier.
#### In future add a flag for all to get and update all designers by business.
#### Use similar logic for a command to update the data, as saving creates new instances.
input1 = 'Bao Bao'
input2 = 'Issey Miyake'

def get_products():
    #TODO: Return file name for scraping site in same format so can select dynamically.
    if input1 == 'Bao Bao':
        return get_bao_bao.main()

#TODO: Would make sense to separate business, designer, and products...
class Command(BaseCommand):
    help = 'Scrape for data'

    def handle(self, *args, **options):
        business_data = get_business.main(input1)

        for designer in business_data['designers']:
            business_designer = Business_Designer(name=designer)

            business_designer.save()

        for category in business_data['categories']:
            category = Category(name=category)

            category.save()

        business = Business(name=business_data['name'], site_url=business_data['site_url'], designer=business_designer, category=category)
        business.save()

        self.stdout.write(self.style.SUCCESS('Successfully saved business.'))

        designer_data = get_designer.main(business_data, input2)

        designer = Designer(name=designer_data['name'], site_url=designer_data['site_url'])

        designer.save()

        self.stdout.write(self.style.SUCCESS('Successfully saved designer.'))

        products_data = get_products()

        for product_data in products_data:
            product_description = product_data['product_description']
            description = Product_Description(name=product_description['name'], season=product_description['season'], collection=product_description['collection'], category=product_description['category'], brand=product_description['brand'])
            description.save()

            product_price = product_data['product_price']
            price = Product_Price(currency=product_price['currency'], amount=float(product_price['amount']))
            price.save()

            product_stock = product_data['stock']
            product_colors = product_stock['colors']
            product_quantities = product_stock['quantities']
            for product_color in product_colors:
                color = Product_Color(color=product_color)
                color.save()

            for product_quantity in product_quantities:
                quantity = Product_Quantity(quantity=product_quantity)
                quantity.save()

            stock = Product_Stock(colors=color, quantities=quantity)
            stock.save()

            product_details = product_data['product_details']
            details = Product_Details(material=product_details['material'], size=product_details['size'], dimensions=product_details['dimensions'], sku=product_details['sku'])
            details.save()

            product_images = product_data['images']
            for product_image in product_images:
                image = Product_Image(image=product_image)
                image.save()

            product = Product(designer=product_data['designer'], product_description=description, product_price=price, site_url=product_data['site_url'], stock=stock, product_details=details, condition=product_data['condition'], image=image)

            product.save()

        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved product data.'))
