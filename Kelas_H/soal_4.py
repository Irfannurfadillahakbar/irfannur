# Program untuk menghitung jumlah huruf vokal dalam kalimat

# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Inisialisasi variabel untuk menghitung jumlah vokal
jumlah_vokal = 0

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal dalam kalimat
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print("Jumlah huruf vokal:", jumlah_vokal)
