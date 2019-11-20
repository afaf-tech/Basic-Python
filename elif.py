#Belajar elif => else if



menu_pilihan = input("Silahkan pilih menu(1-3): ")

# sebenarnya ketika kita memilih menu if maka setiap blok if akan dieksekusi 
# Maka dari itu kita menggunakan else if // tapi di python menggunakan elif keyword
if menu_pilihan=="1":
    print("Anda memilih menu 1")
elif menu_pilihan=="2":
    print("Anda memilih menu 2")
elif menu_pilihan=="3":
    print("Anda memilih menu 3")
else:
    print("menu tidak tersedia")

# Misal di bawah ada if lagi, maka akan dianggap if yang berbeda