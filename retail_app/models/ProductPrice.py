from django.db import models


class ProductPrice(models.Model):
    currency = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=19, decimal_places=2,)

    class Meta:
        verbose_name_plural = "Product Prices"

    def __str__(self):
        return self.currency + str(self.amount)
