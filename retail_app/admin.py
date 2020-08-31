from django.contrib import admin

from .models import (
    Business,
    Designer,
    Product,
    ProductImage,
    ProductStock,
    ProductDescription,
    ProductDetails,
)

admin.site.register(Business)
admin.site.register(Designer)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductStock)
admin.site.register(ProductDescription)
admin.site.register(ProductDetails)
