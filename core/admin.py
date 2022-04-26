from django.contrib import admin
from .models import *


admin.site.register([Image, Category, SubCategory, SubSubCategory])


class ProductImageInline(admin.TabularInline):
    model = Image


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    # raw_id_fields = ['user']


admin.site.register(Product, ProductAdmin)