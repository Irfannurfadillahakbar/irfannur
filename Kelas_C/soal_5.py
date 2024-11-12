# Program untuk mengambil substring dari sebuah kata berdasarkan indeks awal dan akhir

# Meminta pengguna memasukkan sebuah kata
kata = input("Masukkan sebuah kata: ")

# Meminta pengguna memasukkan indeks awal dan akhir
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring berdasarkan indeks yang diberikan
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print("Substring berdasarkan indeks yang diberikan:", substring)

#Shani_Akhmad_Kalani
#2403010072