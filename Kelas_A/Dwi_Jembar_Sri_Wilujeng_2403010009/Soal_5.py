#Dwi Jembar Sri Wilujeng
#2403010009
# Membuat substring dari sebuah kata dengan bahasa pemrograman

# Meminta pengguna untuk memasukkan kata
kata = input("Masukkan kata: ")

# meminta input indeks awal dan akhir
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring dari indeks yang ditentukan
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil
print("Substring:", substring)