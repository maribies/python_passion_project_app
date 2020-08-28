from django.db import models


class ProductStock(models.Model):
    name = models.CharField(max_length=200)
    colors = models.ForeignKey("ProductColor", on_delete=models.CASCADE)
    quantities = models.ForeignKey("ProductQuantity", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Product Stock"

    def __str__(self):
        return str(self.colors) + " - " + str(self.quantities) + " units "
