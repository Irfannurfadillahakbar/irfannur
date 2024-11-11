#Sony Gunawan TI A 24

#menghitung jumlah huruf vokal dalam kalimat
#memasukan kalimat
kalimat = input("masukan kalimat: ")

#huruf vokal
kalimat_vokal = "a,i,u,e,o"

#meneghitung jumlah dalm huruf vokal
kalimat_vokal = sum(1 for char in kalimat if char in kalimat_vokal)

#menampilkan hasil jumlah huruf vokal
print(f"jumlah huruf vokal dalam kalimat: {kalimat_vokal}")