# nama : Surya Alamasyah
# NIM : 2403010001

# Meminta input kata, indeks awal, dan indeks akhir
kata = input("Masukkan kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Substring yang diambil dari indeks awal hingga indeks akhir (tidak termasuk indeks akhir)
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil
print("Substring:", substring)
