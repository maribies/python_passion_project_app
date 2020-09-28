from django.test import TestCase
from scraping import (
    ChanelProducts,
    ChanelHtml,
    ChanelProductBuilder,
    ChanelProductDocument,
    exceptions,
)
from retail_app.management.commands import getchanelproducts


def server_error():
    raise exceptions.ServerError


def not_found():
    raise exceptions.NotFoundError()


class TestGetChanelProducts(TestCase):
    def setUp(self):
        pass

    def test_get_products(self):
        products = getchanelproducts.Command.handle(self)

        assert products is not None


#   TODO: Traceback (most recent call last):
#   File "/Users/marissabiesecker/Desktop/Marissa/Projects/RedSquirrel/python_passion_project_app/python_passion_project/tests/test_Scraper/test_Chanel/test_getchanelproducts.py", line 19, in test_get_products
#     products = getchanelproducts.Command.handle(self)
#   File "/Users/marissabiesecker/Desktop/Marissa/Projects/RedSquirrel/python_passion_project_app/retail_app/management/commands/getchanelproducts.py", line 25, in handle
#     self.stdout.write(
#   AttributeError: 'TestGetChanelProducts' object has no attribute 'stdout'

# TODO: Possible to test exception?
