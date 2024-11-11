#Memotong Substring dari Sebuah Kata
kata = input("Masukkan kata:")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))
substring = kata[indeks_awal:indeks_akhir]
print("Substring:", substring)
