# Meminta input kata dari pengguna
kata = input("Masukkan kata: ")

# Meminta input indeks awal dan indeks akhir
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring berdasarkan indeks yang diberikan
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print(f"Substring: {substring}")