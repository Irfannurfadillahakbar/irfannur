#memotong substring dari sebuah kata

#memasukan input kalimat dengan tipe data string
kalimat = str(input("masukan kalimat: "))

#variabel untuk memasukkan angka sebagai indeks awal pemotongan substring,
# dan menyimpannya dalam variabel 'awal' dengan tipe data integer
awal= int(input("masukan angka awal:"))

#variabel untuk memasukkan angka sebagai indeks akhir pemotongan substring,
# dan menyimpannya dalam variabel 'akhir' dengan tipe data integer
akhir= int(input("masukan angka akhir:"))

#menampilkan kalimat akhir yang sudah di substring
print(kalimat[awal:akhir])