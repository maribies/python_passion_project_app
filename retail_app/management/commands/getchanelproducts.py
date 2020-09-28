from django.core.management.base import BaseCommand, CommandError
from scraping import (
    ChanelHtml,
    ChanelProductBuilder,
    ChanelProductDocument,
    ChanelProducts,
)


class Command(BaseCommand):
    help = "Scrape for Chanel products"

    def handle(self, *args, **options):
        # Get products html from site.
        try:
            products_info = ChanelProducts().get_all_products_info()

            if products_info == [] or products_info is None:
                raise Exception("No products info.")

            # Get html per product.
            for product in products_info:
                url = product.get("url", {})

                html = ChanelHtml(url)

                document = ChanelProductDocument(html.get_html_data(url))

                builder = ChanelProductBuilder(document, product)

                # Create product.
                builder.create_all_product_information()

            self.stdout.write(
                self.style.SUCCESS("Successfully created the Chanel products.")
            )

        except Exception:
            self.stdout.write(self.style.ERROR("Oppps. No products info."))
