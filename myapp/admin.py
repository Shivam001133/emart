from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "dis_price", "categary", "desc")
    # readonly_fields = ("price",)


admin.site.register(Product, ProductAdmin)
