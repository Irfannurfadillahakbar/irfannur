# Program untuk memotong substring dari sebuah kata
# Meminta input kata, indeks awal dan indeks akhir
kata = input("Masukkan kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring dari kata berdasarkan indeks
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print("Substring:", substring
