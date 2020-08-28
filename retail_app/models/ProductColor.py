from django.db import models


class ProductColor(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color
