from retail_app.models import ProductStock
from .color_serializer import ColorSerializer


class StockSerializer:
    def __init__(self, stock: ProductStock):
        self.stock = stock
        self.quantity = stock.quantity

    def to_dict(self):
        return {
            "color": ColorSerializer.to_dict(self.stock),
            "quantity": self.quantity,
        }
