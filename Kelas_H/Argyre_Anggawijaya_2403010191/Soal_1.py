# Nama : Argyre Anggawijaya
# NIM : 2403010191
#  Program untuk menghitung luas dan keliling persegi panjang

def hitung_persegi_panjang():
    try:
        panjang = float(input("Masukkan panjang (cm): "))
        lebar = float(input("Masukkan lebar (cm): "))

        # Menghitung luas dan keliling
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        # Menampilkan hasil
        print(f"Luas persegi panjang: {luas} cm")
        print(f"Keliling persegi panjang: {keliling} cm")
    except ValueError:
        print("Hanya masukkan angka, jangan yang lain :).")
# Memanggil Fungsi
hitung_persegi_panjang()