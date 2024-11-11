#menghitung jumlah huruf vocal --> intanps-2403010017
kalimat=str(input("masukan kalimat anda:"))
vokal="a,i,u,e,o,A,I,U,E,O"
jmlvokal=sum(1 for char in kalimat if char in vokal)
print("jumlah huruf vokalnya:", jmlvokal)