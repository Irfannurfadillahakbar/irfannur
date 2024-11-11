# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Inisialisasi variabel untuk menghitung jumlah vokal
jumlah_vokal = 0

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah vokal dalam kalimat
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print(f"Jumlah huruf vokal dalam kalimat: {jumlah_vokal}")