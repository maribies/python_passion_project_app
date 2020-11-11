from retail_app.models import ProductPrice


class PriceSerializer:
    def __init__(self, price: ProductPrice):
        self.currency = price.currency
        self.amount = price.amount

    def to_dict(self):
        return f"{self.currency}{self.amount}"
