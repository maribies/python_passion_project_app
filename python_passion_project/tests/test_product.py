from django.test import TestCase
from retail_app.models import Product
from model_bakery import baker


class ProductTest(TestCase):
    """Product correctly returns attributes"""

    def setUp(self):
        self.product = baker.make_recipe("retail_app.product_test")

    def test_name(self):
        product = Product.objects.get(name="Test Product")

        self.assertEqual(product.name, "Test Product")

    def test_designer(self):
        product = Product.objects.get(designer="Test Designer")

        self.assertEqual(product.designer, "Test Designer")

    def test_site_url(self):
        product = Product.objects.get(site_url="https://www.testsite.com")

        self.assertEqual(product.site_url, "https://www.testsite.com")

    def test_condition(self):
        product = Product.objects.get(condition="New")

        self.assertEqual(product.condition, "New")

    def test_sku(self):
        details = Product.objects.get(sku="TESTSKU89012")

        self.assertEqual(details.sku, "TESTSKU89012")

    def test_material(self):
        details = Product.objects.get(
            material="test materials made of lots of things"
        )

        self.assertEqual(details.material, "test materials made of lots of things")

    def test_size(self):
        details = Product.objects.get(size="OS")

        self.assertEqual(details.size, "OS")

    def test_dimensions(self):
        details = Product.objects.get(
            dimensions="10in long and 18in wide and 3in depth"
        )

        self.assertEqual(details.dimensions, "10in long and 18in wide and 3in depth")
    
     def test_season(self):
        description = Product.objects.get(season="SS20")

        self.assertEqual(description.season, "SS20")

    def test_collection(self):
        description = Product.objects.get(collection="Test Collection")

        self.assertEqual(description.collection, "Test Collection")

    def test_category(self):
        description = Product.objects.get(category="Handbags")

        self.assertEqual(description.category, "Handbags")

    def test_brand(self):
        description = Product.objects.get(brand="Test Brand")

        self.assertEqual(description.brand, "Test Brand")
