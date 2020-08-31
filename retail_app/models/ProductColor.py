from django.db import models


class ProductColor(models.Model):
    color = models.CharField(max_length=50)
    quantity = models.IntegerField(null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Product Color"

    def __str__(self):
        return str(self.color) + " - " + str(self.quantity)
