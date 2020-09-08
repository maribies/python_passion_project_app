from django.db import models


class ProductDetails(models.Model):
    material = models.TextField()
    size = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=200)
    sku = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Product Details"

    def __str__(self):
        return (
            self.material
            + " - "
            + self.size
            + " - "
            + self.dimensions
            + " - "
            + self.sku
        )
