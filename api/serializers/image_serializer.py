from retail_app.models import ProductImage


class ImageSerializer:
    def __init__(self, image: ProductImage):
        self.image = image

    def to_dict(self):
        return self.image.image_url
