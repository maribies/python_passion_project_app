from django.db import models


class SearchProductKeywords(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    keywords = models.TextField()

    @classmethod
    def create_keywords(cls, product_data, product):
        product_details = product_data["product_details"]
        product_description = product_data["product_description"]
        product_stock = product_data["stock"]

        sku = product_details["sku"]
        product_colors = product_stock["colors"]

        keywords = (
            sku
            + " "
            + product_description["name"]
            + " "
            + product_description["season"]
            + " "
            + product_description["collection"]
            + " "
            + product_description["brand"]
            + " "
            + product_data["designer"]
        )

        keywords += " " + " ".join(product_colors)

        search_keywords = SearchProductKeywords.objects.update_or_create(
            product=product, keywords=keywords
        )

        return search_keywords

    class Meta:
        verbose_name_plural = "Search All Product Keywords"

    def __str__(self):
        return str(self.keywords)
