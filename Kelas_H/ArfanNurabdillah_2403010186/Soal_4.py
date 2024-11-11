# Meminta input kalimat yang ingin di hitung huruf vokalnya
kalimat = input("Masukkan sebuah kalimat: ")

# Inisialisasi variabel untuk menghitung jumlah vokal
jumlah_vokal = 0

# Daftar huruf vokal yang akan dihitung
vokal = "aeiouAEIOU"

# Iterasi setiap karakter dalam kalimat
for karakter in kalimat:
    # Jika karakter adalah huruf vokal, tambahkan 1 ke jumlah_vokal
    if karakter in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print("Jumlah huruf vokal dalam kalimat:", jumlah_vokal)
