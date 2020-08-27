from django.db import models
from django.utils.html import mark_safe


class Business(models.Model):
    name = models.CharField(max_length=50)
    site_url = models.URLField()
    designer = models.ForeignKey("BusinessDesigner", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Businesses"

    def __str__(self):
        return self.name


class BusinessDesigner(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Business Designers"


class Designer(models.Model):
    name = models.CharField(max_length=50)
    site_url = models.URLField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    designer = models.CharField(max_length=100)
    product_description = models.ForeignKey(
        "ProductDescription", on_delete=models.CASCADE
    )
    product_price = models.ForeignKey("ProductPrice", on_delete=models.CASCADE)
    site_url = models.URLField()
    stock = models.ForeignKey("ProductStock", on_delete=models.CASCADE)
    product_details = models.ForeignKey("ProductDetails", on_delete=models.CASCADE)
    CONDITIONS = [(1, "New"), (2, "Preowned")]
    condition = models.CharField(choices=CONDITIONS, max_length=15)
    image = models.ForeignKey("ProductImage", on_delete=models.CASCADE)

    def __str__(self):
        return self.product_description.name


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


class ProductPrice(models.Model):
    currency = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=19, decimal_places=2,)

    class Meta:
        verbose_name_plural = "Product Prices"

    def __str__(self):
        return self.currency + str(self.amount)


class ProductStock(models.Model):
    name = models.CharField(max_length=200)
    colors = models.ForeignKey("ProductColor", on_delete=models.CASCADE)
    quantities = models.ForeignKey("ProductQuantity", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Product Stock"

    def __str__(self):
        return str(self.colors) + " - " + str(self.quantities) + " units "


class ProductColor(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color


class ProductQuantity(models.Model):
    quantity = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.quantity)


class ProductDetails(models.Model):
    material = models.TextField()
    size = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=200)
    sku = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Product Details"

    def __str__(self):
        return (
            self.material
            + " - "
            + self.size
            + " - "
            + self.dimensions
            + " - "
            + self.sku
        )


class Collection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='directory/')

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="150" height="150" />' % self.image)

    image_tag.short_description = 'Image'

    def _str_(self):
        return self.image.title

    class Meta:
        verbose_name_plural = "Product Images"
