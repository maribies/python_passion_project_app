from retail_app.models import ProductPrice
import json


class PriceSerializer:
    def __init__(self, price: ProductPrice):
        self.currency = price.currency
        self.amount = price.amount

    def for_json(self):
        return f"{self.currency}{self.amount}"
