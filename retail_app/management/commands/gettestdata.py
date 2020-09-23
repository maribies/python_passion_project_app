from django.core.management.base import BaseCommand, CommandError
from scraping import get_html
import vcr


@vcr.use_cassette("fixtures/vcr_cassettes/bao_bao.yaml")
def test_bao_bao():
    get_html.get_html_data("https://www.shopbaobaoisseymiyake.com/shop-all")


@vcr.use_cassette("fixtures/vcr_cassettes/chanel.yaml")
def test_chanel():
    get_html.get_html_data("https://www.chanel.com/us/fashion/handbags/c/1x1x1/")


class Command(BaseCommand):
    def handle(self, *args, **options):
        test_bao_bao()
        test_chanel()

        self.stdout.write(self.style.SUCCESS("Cassettes saved."))
