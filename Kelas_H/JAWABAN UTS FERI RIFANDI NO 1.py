# Meminta input panjang dan lebar dari pengguna
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

# Menghitung luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil
print(f"Luas = {luas}")
print(f"Keliling = {keliling}")
