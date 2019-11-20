# Dictionary 
# Objwct Literal pada javascript

# Seperti set tapi punya Indexdefault yang dituliskan progamer
customer = {"name":"Eko","age":30, "address":"Subang"}
name = customer["name"]
age=customer["age"]
address = customer["address"]


# for key in customer:
#     value = customer[key]
#     print(f"{key}:{value}")

# Tambah data baru
customer["Company"] = "Bibli.com"

# Hapus data
# del customer["address"]

# Tuple bisa di ekstrac menjadi dua value
for key, value in customer.items():
    print(f"{key}:{value}")
    # print(f"{key[0]}:{key[1]}")

# items() method adalah data dictionary berupa tuple

print(customer.items())
# hasil
# dict_items([('name', 'Eko'), ('age', 30), ('address', 'Subang')])