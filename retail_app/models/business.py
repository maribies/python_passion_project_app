from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=50)
    site_url = models.URLField()
    designer = models.ForeignKey("BusinessDesigner", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Businesses"

    def __str__(self):
        return self.name
