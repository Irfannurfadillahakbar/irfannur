#Buatlah program yang meminta pengguna untuk memasukkan sebuah kalimat,
# lalu menghitung dan menampilkan jumlah huruf vokal (a, e, i, o, u) di dalam kalimat tersebut.

#Masukan kalimat user
Kalimat = input("Masukan kalimat: ")

# Daftar huruf vokal
vokal = "aeiouAEIOU"

#prosses menghitung huruf vokal
Jumlah_huruf =sum(1 for huruf in Kalimat if huruf in vokal)

#output/hasil dari perhitungan
print(f"Jumlah huruf vokal: {Jumlah_huruf}") 