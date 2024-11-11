# hilman paturohman 2403010029

# Masukan input kalimat apa saja
kalimat = input("Masukkan sebuah kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

# Inisialisasi jumlah vokal
jumlah_vokal = 0

# Menghitung jumlah vokal dalam kalimat
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

# output
print("Jumlah huruf vokal dalam kalimat:", jumlah_vokal)
