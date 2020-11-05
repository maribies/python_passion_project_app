from retail_app.models import ProductColor
import json


class ColorSerializer:
    def __init__(self, color: ProductColor):
        self.color = color

    def to_json(self):
        return self.color.color
