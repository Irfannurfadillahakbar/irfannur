kalimat = input("Masukkan sebuah kalimat: ")

vokal = "aeiouAEIOU"
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

print("Jumlah huruf vokal dalam kalimat:", jumlah_vokal)