from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity')

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('material', 'remainder','for_check_remainder_count', 'price')