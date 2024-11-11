def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

# Input dari pengguna
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

luas, keliling = hitung_persegi_panjang(panjang, lebar)

print(f"Luas persegi panjang: {luas} cm²")
print(f"Keliling persegi panjang: {keliling} cm")