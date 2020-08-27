from django.contrib import admin

from .models import Business, Designer, Product, ProductImage

admin.site.register(Business)
admin.site.register(Designer)
admin.site.register(Product)
admin.site.register(ProductImage)
