from retail_app.models import ProductStock
from .color_serializer import ColorSerializer
import json


class StockSerializer:
    def __init__(self, stock: ProductStock):
        self.stock = stock
        self.quantity = stock.quantity

    def for_json(self):
        return {
            "color": ColorSerializer.for_json(self.stock),
            "quantity": self.quantity,
        }
