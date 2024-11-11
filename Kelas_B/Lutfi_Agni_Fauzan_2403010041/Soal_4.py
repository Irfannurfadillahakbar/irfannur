#menghitung jumlah huruf vokal pada suatu kalimat

#variabel input kalimat dengan tipe data string
kalimat = str(input("masukan kalimat: "))

#mendefinisikan setiap huruf vokal besar dan kecil
vokal ="a,i,u,e,o,A,I,U,E,O"

#menghitung setiap kalimat yang memiliki huruf vokal
jumlah_vokal= sum(1 for char in kalimat if char in vokal)

#menampilkan jumlah huruf vokal
print("jumalh huruf vokal: ",jumlah_vokal)