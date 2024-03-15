from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouse

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'code']




