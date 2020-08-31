from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    designer = models.CharField(max_length=100)
    product_description = models.ForeignKey(
        "ProductDescription", on_delete=models.CASCADE
    )
    product_price = models.ForeignKey("ProductPrice", on_delete=models.CASCADE)
    site_url = models.URLField()
    product_details = models.ForeignKey("ProductDetails", on_delete=models.CASCADE)
    CONDITIONS = [(1, "New"), (2, "Preowned")]
    condition = models.CharField(choices=CONDITIONS, max_length=15)

    def __str__(self):
        return self.product_description.name
