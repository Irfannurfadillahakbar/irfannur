# Meminta input dari pengguna
kata = input("Masukkan sebuah kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mendapatkan substring dari indeks awal hingga indeks akhir (tidak termasuk indeks akhir)
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print("Substring yang diambil:", substring)
