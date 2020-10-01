from django.db import models


class ProductsManager(models.Manager):
    def fully_loaded_objects(self):
        return (
            super()
            .get_queryset()
            .order_by("designer")
            .select_related("product_price")
            .prefetch_related("productimage_set")
            .prefetch_related("productstock_set__color")
        )
