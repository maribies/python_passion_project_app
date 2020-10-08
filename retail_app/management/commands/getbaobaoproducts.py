from django.core.management.base import BaseCommand, CommandError
from scraping import (
    BaoBaoProducts,
    BaoBao,
)


class Command(BaseCommand):
    help = "Scrape for Bao Bao products"

    def handle(self, *args, **options):
        try:
            products_urls = BaoBaoProducts().get_products_urls()

            products_total = BaoBao.create_products(self, products_urls)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created {products_total} Bao Bao products."
                )
            )

        except Exception as e:
            self.stdout.write(self.style.ERROR("Opps"))
            self.stdout.write(self.style.ERROR(e))
