from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse


class ProductMaterialInline(admin.TabularInline):
    model = ProductMaterial
    extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id",'name', 'code')
    inlines = [ProductMaterialInline]


class WarehouseInline(admin.TabularInline):
    model = Warehouse
    extra = 2


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("id",'name',)
    inlines = [WarehouseInline]


@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ("id",'product', 'material', 'quantity')


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("id",'material', 'remainder', 'for_check_remainder_count', 'price')
