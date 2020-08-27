from django.db import models


class ProductQuantity(models.Model):
    quantity = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.quantity)
