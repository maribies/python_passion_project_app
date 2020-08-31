from django.db import models


class ProductStock(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    color_stock = models.ForeignKey("ProductColor", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Product Stock"

    def __str__(self):
        return str(self.product) + " - " + str(self.color_stock)
