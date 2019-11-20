#  Belajar membuat meethod / Function
# Pastikan saat membuat method, pemanggilan harus dilakukan setelah pembuatan methodnya
# DUE TO program berparadigma perocedural menggunakan pembacaan dari atas ke bawah
nama=[]

def print_nama():
    print("======")
    for data in nama:
        print(data)


nama.append("eko")
print_nama()

nama.append("Yuda")
print_nama()

nama.append("Juang")
print_nama()