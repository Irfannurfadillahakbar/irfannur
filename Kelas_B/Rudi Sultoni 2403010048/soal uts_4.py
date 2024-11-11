print("Menghitung Jumlah Huruf Vokal dalam Kalimat")
print()
kalimat= input("masukan kalimat: ")
huruf_vokal= "AIUEOaiueo"
jumlah_vokal= sum(1 for huruf in kalimat if huruf in huruf_vokal)
print("jumlah huruf vokal",jumlah_vokal)
