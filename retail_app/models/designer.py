from django.db import models


class Designer(models.Model):
    name = models.CharField(max_length=50)
    site_url = models.URLField()

    def __str__(self):
        return self.name
