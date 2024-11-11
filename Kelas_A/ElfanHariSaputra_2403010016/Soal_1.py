# Nama: Elfan Hari Saputra
# NIM: 2403010016
# Kelas: TI-A-24
# Deskripsi: Program ini berfungsi untuk menghitung luas dan keliling persegi panjang, user diminta untuk input panjang dan lebar

print('--- Menghitung Luas dan Keliling Persegi Panjang ---') # judul program,cuma layouting :D
print('') # agar ada jarak setelah judul

panjang = float(input("Berapa panjangnya?: ")) # input panjang
lebar = float(input("Berapa lebarnya?: ")) # input lebar
luas = panjang * lebar # hitung luas
keliling = 2 * (panjang + lebar) # hitung keliling

print("Luas:", luas) # show luas
print("Keliling:", keliling) # show keliling
