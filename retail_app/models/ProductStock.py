from django.db import models


class ProductStock(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    color = models.ForeignKey("ProductColor", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Product Stock"

    def __str__(self):
        return str(self.product) + " - " + str(self.color) + " - " + str(self.quantity)
