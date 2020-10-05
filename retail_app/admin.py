from django.contrib import admin

from .models import (
    Designer,
    Product,
    ProductImage,
    ProductStock,
    SearchProductKeywords,
)

admin.site.register(Designer)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductStock)
admin.site.register(SearchProductKeywords)
