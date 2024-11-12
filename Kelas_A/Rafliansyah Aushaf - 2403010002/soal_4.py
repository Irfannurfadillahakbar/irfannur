#Menghitung Jumlah Huruf Vokal dalam Kalimat
kalimat = input("Masukan Kalimat: ")
jumlah_vokal = 0
vokal = "a, i, u, e, o"
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1
print("jumlah huruf vokal dalam kalimat:", jumlah_vokal)