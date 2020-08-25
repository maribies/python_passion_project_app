from django.contrib import admin

from .models import Business, Designer, Category, Product, Product_Description, Product_Price, Product_Stock, Product_Details, Collection, Season, Product_Image

admin.site.register(Business)
admin.site.register(Designer)
admin.site.register(Product)
admin.site.register(Product_Image)
