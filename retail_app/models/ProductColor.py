from django.db import models


class ProductColor(models.Model):
    color = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Product Color"

    def __str__(self):
        return str(self.color)
