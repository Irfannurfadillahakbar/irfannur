# NAMA : BIMO ALVIANA SOPIAN
# NIM  : 2403010071
# KELAS: C
kalimat = input("Selamat datang di dunia pemrograman: ")

jumlah_vokal = 0

vokal = "aeiouAEIOU"

for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

print(f"13: {jumlah_vokal}")
