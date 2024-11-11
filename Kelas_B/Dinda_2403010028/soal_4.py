#menghitung jumlah huruf vocal = dindadinna 2403010028
kalimat=str(input("masukan kalimat anda:"))
vokal=",A,I,U,E,O,a,i,u,e,o"
jmlvokal=sum(1 for char in kalimat if char in vokal)
print("jumlah huruf vokalnya:", jmlvokal)