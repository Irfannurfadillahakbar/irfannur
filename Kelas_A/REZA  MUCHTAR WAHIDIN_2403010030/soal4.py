#Menghitung Jumlah Huruf Vokal dalam Kalimat
kalimat = input("masukan kalimat: ")
jumlah_huruf_vokal = 0
vokal = "aiueoAIUEO"
for huruf in kalimat :
    if huruf in vokal:
        jumlah_huruf_vokal += 1
print("jumlah huruf vokal :", jumlah_huruf_vokal)
