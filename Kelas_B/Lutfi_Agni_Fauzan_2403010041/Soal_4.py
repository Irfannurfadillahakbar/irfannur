kalimat = str(input("masukan kalimat: "))

vokal ="a,i,u,e,o,A,I,U,E,O"
jumlah_vokal= sum(1 for char in kalimat if char in vokal)

print("jumalh huruf vokal: ",jumlah_vokal)