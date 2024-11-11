# Meminta input dari pengguna
kata = input("Masukkan kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring dari indeks awal hingga indeks akhir (tidak termasuk indeks akhir)
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil
print("Substring:", substring)
