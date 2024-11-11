
# Meminta input dari pengguna untuk panjang dan lebar
panjang = float(input("Masukkan panjang persegi panjang (dalam satuan cm): "))
lebar = float(input("Masukkan lebar persegi panjang (dalam satuan cm): "))

# Menghitung luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil
print(f"Luas persegi panjang adalah: {luas} cm²")
print(f"Keliling persegi panjang adalah: {keliling} cm")
