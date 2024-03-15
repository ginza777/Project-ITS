from django.db import models

from .models import Product, ProductMaterial, Warehouse


class GetMaterials:
    def __init__(self, request_data):
        self.reset_db()
        self.products_data = request_data

    def get_products_data(self):
        products_datas = self.products_data
        result = []
        for product_data in products_datas:
            product = Product.objects.get(id=product_data['id'])
            product_materials = ProductMaterial.objects.filter(product=product)
            count = product_data['count']
            result_data = {
                "product_name": product.name,
                "product_qty": count,
            }
            print(f"Bizga {count} ta {product.name} uchun  kerak:")
            for product_material in product_materials:
                print(
                    f"{product_material.material.name} - {product_material.quantity * count}  omborda borligi: {Warehouse.objects.filter(material=product_material.material).aggregate(models.Sum('for_check_remainder_count'))}  ")

            material_data_list = []
            print(100*'-_')
            for product_material in product_materials:
                p_material = product_material.material  # material nomi
                warehouse_material_remainders = Warehouse.objects.filter(material=p_material)  # material qolgan miqdori
                warehouse_material_remainders_summ = Warehouse.objects.filter(material=p_material).aggregate(
                    models.Sum('for_check_remainder_count'))  # material qolgan miqdori

                if warehouse_material_remainders_summ[
                    'for_check_remainder_count__sum'] < product_material.quantity * count:
                    material_data = {
                        "warehouse_id": None,
                        "material_name": f"{p_material.name}",
                        "qty": product_material.quantity * count - warehouse_material_remainders_summ[
                            'for_check_remainder_count__sum'],
                        "price": None
                    }
                    material_data_list.append(material_data)
                    p_count = product_material.quantity * count - warehouse_material_remainders_summ[
                        'for_check_remainder_count__sum']

                    for warehouse_material_remainder in warehouse_material_remainders:
                        if warehouse_material_remainder.for_check_remainder_count >= p_count > 0:
                            material_data = {
                                "warehouse_id": warehouse_material_remainder.id,
                                "material_name": f"{p_material.name}",
                                "qty": p_count,
                                "price": warehouse_material_remainder.price
                            }
                            material_data_list.append(material_data)
                            warehouse_material_remainder.for_check_remainder_count -= p_count
                            warehouse_material_remainder.save()
                            p_count = 0
                        if 0 < warehouse_material_remainder.for_check_remainder_count < p_count:
                            material_data = {
                                "warehouse_id": warehouse_material_remainder.id,
                                "material_name": f"{p_material.name}",
                                "qty": warehouse_material_remainder.for_check_remainder_count,
                                "price": warehouse_material_remainder.price
                            }
                            p_count -= warehouse_material_remainder.for_check_remainder_count
                            warehouse_material_remainder.for_check_remainder_count = 0
                            material_data_list.append(material_data)
                            warehouse_material_remainder.save()
                        result_data['product_materials'] = material_data_list

                else:
                    p_count = product_material.quantity * count
                    for warehouse_material_remainder in warehouse_material_remainders:

                        if warehouse_material_remainder.for_check_remainder_count >= p_count > 0:
                            material_data = {
                                "warehouse_id": warehouse_material_remainder.id,
                                "material_name": f"{p_material.name}",
                                "qty": p_count,
                                "price": warehouse_material_remainder.price
                            }
                            material_data_list.append(material_data)
                            warehouse_material_remainder.for_check_remainder_count -= p_count
                            warehouse_material_remainder.save()
                            p_count = 0

                        if 0 < warehouse_material_remainder.for_check_remainder_count < p_count:
                            material_data = {
                                "warehouse_id": warehouse_material_remainder.id,
                                "material_name": f"{p_material.name}",
                                "qty": warehouse_material_remainder.for_check_remainder_count,
                                "price": warehouse_material_remainder.price
                            }
                            p_count -= warehouse_material_remainder.for_check_remainder_count

                            warehouse_material_remainder.for_check_remainder_count = 0

                            warehouse_material_remainder.save()

                            material_data_list.append(material_data)

                        result_data['product_materials'] = material_data_list
                        warehouse_material_remainder.save()

            result.append(result_data)
        print(result)
        return result

    def reset_db(self):
        Warehouse.objects.all().update(for_check_remainder_count=models.F('remainder'))
