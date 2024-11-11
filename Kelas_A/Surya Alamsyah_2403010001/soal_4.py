# nama : Surya Alamsyah
# NIM : 2403010001


# Meminta input
kalimat = input("Masukkan kalimat: ")

# Jumlah vokal
jumlah_vokal = 0

# Huruf vokal
vokal = "aeiouAEIOU"

# Menghitung
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

# Menampilkan hasil
print("Jumlah huruf vokal:", jumlah_vokal)
