# Meminta input kata indeks
kata = input("Masukkan sebuah kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring berdasarkan indeks awal dan akhir
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print("Substring:", substring)
