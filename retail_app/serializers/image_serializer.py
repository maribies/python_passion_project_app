from retail_app.models import ProductImage
import json


class ImageSerializer:
    def __init__(self, image: ProductImage):
        self.image = image

    def for_json(self):
        return self.image.image_url
