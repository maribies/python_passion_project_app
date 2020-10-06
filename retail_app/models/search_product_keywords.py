from django.db import models
from django.contrib.postgres.indexes import GistIndex


class SearchProductKeywords(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    keywords = models.TextField()

    class Meta:
        verbose_name_plural = "Search All Product Keywords"

        indexes = [GistIndex(fields=["keywords"])]

    def __str__(self):
        return str(self.keywords)
