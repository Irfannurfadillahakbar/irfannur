# Fathan Mufti Fadlillah
# NIM: 2403010012
# KELAS A

# Program untuk Memotong Substring dari Sebuah Kata

# Meminta pengguna untuk memasukkan sebuah kata
kata = input("Masukkan kata: ")

# Meminta input indeks awal dan akhir
index_awal = int(input("Masukkan indeks awal: "))
index_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring berdasarkan input dari pengguna
substring = kata[index_awal:index_akhir]

# Menampilkan hasil
print(f"Substring: {substring}")