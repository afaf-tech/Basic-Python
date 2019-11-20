# Return Value
# Procedure = Method yang hanya mengeksekusi 
# Function  - Method yg mengembalikan nilai

def Jumlahin(*list_angka):
    total=0
    for angka in list_angka:
        total = total + angka
    # print(f"Total {list_angka} = {total}")
    # return type berupa tuple
    return (list_angka, total)

# karena return value ada dua maka saat pemanggilan harus dimasukkan ke dalam dua variable
list_angka, total = Jumlahin(10,10,2,2,4)


# Mengambil data total???????????BIG QUESTIONMARK
print(f"Total {list_angka} {total}")