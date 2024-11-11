# Dida Ferdiana 2403010005
# input kata atau kalimat
kata = input ("masukkan kata: ")

# daftar vokal
vokal = ["a", "e", "i", "o", "u"]

# Variabel jumlah_vokal diinisialisasi dengan nilai 0
jumlah_vokal = 0

# Kode ini adalah loop for yang memeriksa setiap huruf dalam variabel kata.
# Jika huruf tersebut termasuk dalam daftar vokal, maka jumlah_vokal ditambahkan 1.
for huruf in kata:
    if huruf in vokal:
        jumlah_vokal += 1

# output
print ("jumlah huruf vokal: ", jumlah_vokal)
