from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    designer = models.CharField(max_length=100)
    product_price = models.ForeignKey("ProductPrice", on_delete=models.CASCADE)
    site_url = models.URLField()
    CONDITIONS = [(1, "New"), (2, "Preowned")]
    condition = models.CharField(choices=CONDITIONS, max_length=15)
    material = models.TextField()
    size = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=200)
    sku = models.CharField(max_length=50)
    season = models.CharField(max_length=50, null=True, blank=True)
    collection = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
