# Belajar argument list


print("Tanpa argumentList")
def jumlahkan(satu, dua, tiga=0):
    total = satu + dua + tiga
    print(f"total {[satu, dua, tiga]} = {total}")

jumlahkan(10,10,10)

print("Dengan ArgumentList")
# Means argument akan berubah menjadi list
# Jikaingin memasukkan dua parameter dan yang satu bukan bagian dari argList maka ditaruh di paling depan
def Jumlahin(*list_angka):
    total=0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")

Jumlahin(10,10,2,2,4)