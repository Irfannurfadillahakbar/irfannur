kalimat =input("masukan kalimat:")
vokal ="aiueoAIUEO"
jumlah_vokal =sum(1 for huruf in kalimat if huruf in vokal)
print("jummlah huruf vokal",jumlah_vokal)