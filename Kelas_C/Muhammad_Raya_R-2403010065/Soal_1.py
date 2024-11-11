print("\nPROGRAM MENGHITUNG LUAS DAN KELILING\n")

# input
panjang = input("masukkan panjang: ")
lebar = input("masukkan lebar: ")
# rumus
# disini saya menggunkan int(), untuk mengkonversi dari input yang berbentuk string
luas = int(panjang)*int(lebar)
keliling = 2* int((panjang + lebar))
# output
print('luas persegi panjang : ', luas)
print('keliling persegi panjang : ', keliling)
