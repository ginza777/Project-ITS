from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.code or self.code == '' or self.code == 'None':
            self.code = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'product'
        verbose_name = 'product'


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'material'
        verbose_name_plural = 'material'
        verbose_name = 'material'


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.product.name)

    class Meta:
        db_table = 'product_material'
        verbose_name_plural = 'product_material'
        verbose_name = 'product_material'


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    for_check_remainder_count = models.FloatField()
    remainder = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return str(self.material.name)

    class Meta:
        db_table = 'warehouse'
        verbose_name_plural = 'warehouse'
        verbose_name = 'warehouse'
