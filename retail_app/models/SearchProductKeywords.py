from django.db import models


class SearchProductKeywords(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    keywords = models.TextField()

    class Meta:
        verbose_name_plural = "Search All Product Keywords"

    def __str__(self):
        return str(self.keywords)
