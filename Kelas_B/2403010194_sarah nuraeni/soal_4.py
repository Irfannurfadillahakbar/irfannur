#Nama       : Sarah nuraeni
#NIM        : 2403010194
#Deskrifsi  : Program ini meminta pengguna untuk memasukkan sebuah kata lalu menghitung dan menampilkan huruf vokal yang ada dalam kata tersebut

kalimat = input("masukkan sebuah kalimat: ")

vokal = "a,i,u,e,o,A,I,U,E,O"

jumlah_vokal = sum(1 for char in kalimat if char in vokal)

print(f"jumlah huruf vokal dalam kalimat: {jumlah_vokal}")
