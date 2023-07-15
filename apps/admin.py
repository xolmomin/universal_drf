from django.contrib import admin
from apps.models import Photo, Product


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass

