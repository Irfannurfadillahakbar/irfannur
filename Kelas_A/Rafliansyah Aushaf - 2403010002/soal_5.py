#Memotong Substring dari Sebuah Kata
kata = input("Masukan kata:")
indeks_awal = int(input("Masukan indeks awal: "))
indeks_akhir = int(input("Masukan indeks akhir: "))
substring = kata[indeks_awal:indeks_akhir]
print("substring:", substring)