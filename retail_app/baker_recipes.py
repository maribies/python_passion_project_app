from model_bakery.recipe import Recipe, foreign_key
from retail_app.models import (
    Collection,
    Designer,
    ProductPrice,
    Product,
    ProductColor,
    ProductImage,
    ProductStock,
    SearchProductKeywords,
    Season,
)
from decimal import Decimal

collection_test = Recipe(Collection, name="Test Collection")

designer_test = Recipe(
    Designer, name="Test Designer", site_url="https://www.testdesignersite.com"
)

price_test = Recipe(ProductPrice, currency="$", amount=Decimal("1234.56"))

product_test = Recipe(
    Product,
    name="Test Product",
    designer="Test Designer",
    site_url="https://www.testsite.com",
    condition="New",
    season="SS20",
    collection="Test Collection",
    category="Handbags",
    brand="Test Brand",
    material="test materials made of lots of things",
    size="OS",
    dimensions="10in long and 18in wide and 3in depth",
    sku="TESTSKU89012",
    product_price=foreign_key(price_test),
)

color_test = Recipe(ProductColor, color="purple")

image_test = Recipe(
    ProductImage,
    image_url="https://www.imageurl.jpeg",
    product=foreign_key(product_test),
)

stock_test = Recipe(
    ProductStock,
    product=foreign_key(product_test),
    color=foreign_key(color_test),
    quantity=1,
)

search_test = Recipe(
    SearchProductKeywords,
    product=foreign_key(product_test),
    keywords="some keywords to search for things in a string",
)

season_test = Recipe(Season, name="SS20")
