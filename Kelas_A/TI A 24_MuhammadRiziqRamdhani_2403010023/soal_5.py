print("Nama : Muhammad Riziq Ramdhani")
print("NIM  : 2403010023")
print("------------------------------------------")

# Memotong Substring dari Sebuah Kata
kata = input("Masukkan kata: ")

# inisialisasi indeks awal dan akhir
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# substring
substring = kata[indeks_awal:indeks_akhir]
# Menampilkan hasil substring
print(f"substring dari indeks {indeks_awal} hingga {indeks_akhir} adalah:{substring}")

print("------------------------------------------")