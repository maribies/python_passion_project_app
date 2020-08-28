from django.db import models


class ProductDescription(models.Model):
    name = models.CharField(max_length=200)
    season = models.CharField(max_length=50)
    collection = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.category + " - " + self.name

    class Meta:
        verbose_name_plural = "Product Description"
