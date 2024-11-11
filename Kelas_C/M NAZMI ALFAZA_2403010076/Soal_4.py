kalimat =input("Masukan kalimat: ")
jumlah_vokal = 0
vokal= "aeiouAEIOU"
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal += 1

print("/Jumlah huruf vokal:", jumlah_vokal)
