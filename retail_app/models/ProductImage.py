from django.db import models
from django.utils.html import mark_safe


class ProductImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="directory/")

    def image_tag(self):
        return mark_safe(
            '<img src="/directory/%s" width="150" height="150" />' % self.image
        )

    image_tag.short_description = "Image"

    def _str_(self):
        return self.image.title

    class Meta:
        verbose_name_plural = "Product Images"
