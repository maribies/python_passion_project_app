from django.db import models


class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    image_url = models.TextField(null=False)

    class Meta:
        verbose_name_plural = "Product Images"

    def __str__(self):
        return str(self.product) + " image"
