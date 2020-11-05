from retail_app.models import Product
from . import (
    PriceSerializer,
    ImageSerializer,
    StockSerializer,
)
import json


class ProductSerializer:
    def __init__(self, product: Product):
        self.product = product

    def product_stock(self):
        return self.product.productstock_set.all()

    def product_images(self):
        return self.product.productimage_set.all()

    def to_json(self):
        return json.dumps(
            {
                "name": self.product.name,
                "designer": self.product.designer,
                "site_url": self.product.site_url,
                "condition": self.product.condition,
                "season": self.product.season,
                "collection": self.product.collection,
                "category": self.product.category,
                "brand": self.product.brand,
                "material": self.product.material,
                "size": self.product.size,
                "dimensions": self.product.dimensions,
                "sku": self.product.sku,
                "product_price": PriceSerializer(self.product.product_price).to_json(),
                "stock": [
                    StockSerializer(stock).to_json() for stock in self.product_stock()
                ],
                "images": [
                    ImageSerializer(image).to_json() for image in self.product_images()
                ],
            }
        )
