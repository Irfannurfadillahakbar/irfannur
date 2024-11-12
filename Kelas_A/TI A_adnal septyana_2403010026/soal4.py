# Meminta input kalimat dari pengguna
kalimat = input("Masukkan sebuah kalimat: ")

# Inisialisasi variabel untuk menghitung jumlah huruf vokal
jumlah_vokal = 0

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal dalam kalimat
for char in kalimat:
    if char in vokal:
        jumlah_vokal += 1

# Menampilkan jumlah huruf vokal
print(f"Jumlah huruf vokal dalam kalimat: {jumlah_vokal}")