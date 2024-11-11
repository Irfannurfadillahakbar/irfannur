kalimat = input("masukkan kalimat:")
vokal = "aiueoAIUEO"
jumlah_vokal =sum(1 for huruf in kalimat if huruf in vokal)
print("Jumlah huruf vokal",jumlah_vokal)