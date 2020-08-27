from django.contrib import admin

from .models import Business, Designer, Product, ProductStock, ProductColor, ProductImage, ProductDescription, ProductDetails, ProductPrice, ProductQuantity

admin.site.register(Business)
admin.site.register(Designer)
admin.site.register(Product)
admin.site.register(ProductStock)
admin.site.register(ProductColor)
admin.site.register(ProductImage)
admin.site.register(ProductDescription)
admin.site.register(ProductDetails)
admin.site.register(ProductPrice)
admin.site.register(ProductQuantity)

fields = ['image_tag']
readonly_fields = ['image_tag']
