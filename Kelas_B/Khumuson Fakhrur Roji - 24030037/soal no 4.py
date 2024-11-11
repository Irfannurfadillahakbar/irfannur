kalimat = input ("masukan sebuah kalimat: ")
vokal = "a,i,u,e,o"
jum_vokal = sum(1 for char in kalimat if char in vokal)
print(f"jumlah huruf vokal dalam kalimat: {jum_vokal}")