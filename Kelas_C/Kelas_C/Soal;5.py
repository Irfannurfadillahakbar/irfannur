# Meminta input kata dari pengguna
kata = input("Masukkan sebuah kata: ")

# Meminta input indeks awal dan indeks akhir
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring berdasarkan indeks yang diberikan
# Ingat bahwa indeks akhir tidak termasuk, jadi gunakan slicing [start:end]
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print(f"Substring yang diambil: {substring}")

# Menampilkan hasil
print(f"Jumlah huruf vokal dalam kalimat: {jumlah_vokal}")