from django.test import TestCase
from retail_app.management.commands import createdesigner
from scraping import CreateDesigner


class TestCreateDesigner(TestCase):
    def setUp(self):
        self.name = "Issey Miyake"
        self.url = "https://www.shopbaobaoisseymiyake.com/"

    # TODO: Can't seem to be able to figure out how to pass options.
    # def test_handle(self):
    #     options = {'name': self.name, 'url': self.url}

    #     designer = createdesigner.Command.handle(self, options, options)

    #     self.assertIsInstance(designer, CreateDesigner)
    #     self.assertEqual(type(designer.name), str)
    #     self.assertEqual(type(designer.url), str)
    #     self.assertEqual(designer.name, "Issey Miyake")
    #     self.assertEqual(designer.url, "https://www.shopbaobaoisseymiyake.com/")
