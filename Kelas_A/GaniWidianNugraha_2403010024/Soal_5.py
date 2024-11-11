#Buatlah program yang meminta pengguna memasukkan sebuah kata dan dua bilangan bulat, yaitu indeks awal dan indeks akhir.
# Program harus mengeluarkan substring dari kata tersebut berdasarkan indeks awal dan akhir yang diberikan.

#masukan input user
Kata = input("Masukan kata: ")
indeks_awal = int(input("masukan indeks awal: "))
indeks_akhir = int(input("masukan indeks akhir: "))

#mengambil substring dari kata
substring = Kata[indeks_awal : indeks_akhir]

#utput/hasil substring
print(f"substring: {substring}")