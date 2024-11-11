#Menghitung Jumlah Huruf Vokal dalam Kalimat
kalimat = input("Masukkan kalimat: ")
jumlah_vokal = 0
vokal = "aiueoAIUEO"
for huruf in kalimat:
  if huruf in vokal:
    jumlah_vokal += 1
print("Jumlah huruf vokal dalam kalimat:", jumlah_vokal)
