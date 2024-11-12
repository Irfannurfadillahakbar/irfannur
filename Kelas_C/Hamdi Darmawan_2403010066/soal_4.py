# Program untuk menghitung jumlah huruf vokal dalam kalimat
kalimat = input("Masukkan kalimat: ")
vokal = "aeiouAEIOU"
jumlah_vokal = 0
for huruf in kalimat:
    if huruf in vokal:
        jumlah_vokal +=1


print("Jumlah huruf vokal:", jumlah_vokal)
