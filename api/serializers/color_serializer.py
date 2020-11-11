from retail_app.models import ProductColor


class ColorSerializer:
    def __init__(self, color: ProductColor):
        self.color = color

    def to_dict(self):
        return self.color.color
