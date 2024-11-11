kata = input("Masukkan sebuah kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

substring = kata[indeks_awal:indeks_akhir]

print("Substring dari indeks awal hingga indeks akhir:", substring)