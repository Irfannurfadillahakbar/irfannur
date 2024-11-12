# Meminta pengguna untuk memasukkan kalimat
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal
jumlah_vokal = 0
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print("Jumlah huruf vokal dalam kalimat adalah:", jumlah_vokal)
