from django.contrib import admin

from .models import (
    Business,
    Designer,
    Product,
)

admin.site.register(Business)
admin.site.register(Designer)
admin.site.register(Product)


fields = ["image_tag"]
readonly_fields = ["image_tag"]
