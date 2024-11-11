# Meminta input dari pengguna
kata=(input("masukkan kata:"))
indeks_awal=int(input("masukkan indeks awal:"))
indeks_akhir=int(input("masukkan indeks akhir:"))
# Mengambil substring berdasarkan indeks awal dan akhir
substring=kata[indeks_awal:indeks_akhir]
# Menampilkan hasil
print("substring:",substring)