# Meminta input dari pengguna
kata =input("Masukkan kata: ")
indeks_awal = int(input("Masukkan indeks_awal: "))
indeks_akhir = int(input("Masukkan indeks_akhir: "))

# Mengambil substring dari kata sesuai indeks yang diberikan 
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil akhir
print("Substring:", substring)
