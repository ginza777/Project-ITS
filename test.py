# Ma'lumotlar bazasi
omborxonalar = [
    {"material_id": 1, "remainder": 12, "price": 1500},
    {"material_id": 1, "remainder": 200, "price": 1600},
    {"material_id": 2, "remainder": 40, "price": 500},
    {"material_id": 2, "remainder": 300, "price": 550},
    {"material_id": 3, "remainder": 500, "price": 300},
    {"material_id": 4, "remainder": 1000, "price": 2000}
]

# So'rov javobi
javob = []

# Mahsulotlar va ularning xomashyolari
mahsulotlar = [
    {"product_name": "Koylak", "product_qty": 30, "materials": [
        {"material_id": 1, "required_qty": 24},
        {"material_id": 5, "required_qty": 150},
        {"material_id": 3, "required_qty": 40}
    ]},
    {"product_name": "Shim", "product_qty": 20, "materials": [
        {"material_id": 1, "required_qty": 28},
        {"material_id": 4, "required_qty": 40},
        {"material_id": 6, "required_qty": 20}
    ]}
]

# Omborxonadagi ma'lumotlarni tekshirish va javobni tayyorlash
for mahsulot in mahsulotlar:
    product_name = mahsulot["product_name"]
    product_qty = mahsulot["product_qty"]
    product_materials = []

    for material in mahsulot["materials"]:
        material_id = material["material_id"]
        required_qty = material["required_qty"]

        remainder = 0
        price = None
        warehouse_id = None

        for omborxona in omborxonalar:
            if omborxona["material_id"] == material_id:
                if omborxona["remainder"] >= required_qty:
                    remainder = required_qty
                    price = omborxona["price"]
                    warehouse_id = omborxona["material_id"]
                else:
                    remainder = omborxona["remainder"]
                    price = omborxona["price"]
                    warehouse_id = omborxona["material_id"]
                    required_qty -= omborxona["remainder"]

        product_materials.append({
            "warehouse_id": warehouse_id,
            "material_name": "Mato" if material_id == 1 else "Tugma" if material_id == 5 else "Ip" if material_id in [3,
                                                                                                                      4] else "Zamok",
            "qty": remainder,
            "price": price
        })

    javob.append({
        "product_name": product_name,
        "product_qty": product_qty,
        "product_materials": product_materials
    })

print(javob)
